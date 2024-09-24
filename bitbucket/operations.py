"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
import json
import os
from zipfile import ZipFile
import shutil
from django.conf import settings
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError
from connectors.cyops_utilities.files import download_file_from_cyops, check_file_traversal, save_file_in_env
from .constants import *

logger = get_logger('gitlab')


class BitBucket:
    def __init__(self, config):
        self.server_url = config.get('server_url').strip('/')
        if not (self.server_url.startswith('https://') or self.server_url.startswith('http://')):
            self.server_url = 'https://' + self.server_url
        self.username = config.get('username')
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl')

    def make_request(self, endpoint, method='GET', data=None, params=None, files=None, headers=None, validate_username=False):
        try:
            url = self.server_url + endpoint
            logger.info('Executing url {}'.format(url))
            auth = None
            if not headers:
                headers = {
                    'Authorization': "Bearer {0}".format(self.api_key),
                    'content-type': 'application/json'
                }
            if validate_username:
                headers = {
                    'content-type': 'application/json'
                }
                auth = (self.username, self.api_key)
            # CURL UTILS CODE
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, url, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.debug(f"Error in curl utils: {str(err)}")

            response = requests.request(method, url, params=params, files=files, data=data, headers=headers,
                                        verify=self.verify_ssl, auth=auth)
            if response.ok:
                logger.info('successfully get response for url {}'.format(url))
                if method.lower() == 'delete' or response.status_code == 204:
                    return response
                else:
                    if response.status_code == 304:
                        return None
                return response.json()
            elif response.status_code == 400:
                error_response = response.json()
                error_description = error_response['message'] if error_response.get('message') else error_response
                raise ConnectorError({'error_description': error_description})
            elif response.status_code == 401:
                error_response = response.json()
                if error_response.get('errors'):
                    error_description = error_response['errors']
                elif error_response.get('message'):
                    error_description = error_response['message']
                else:
                    error_description = error_response
                raise ConnectorError({'error_description': error_description})
            elif response.status_code == 404:
                error_response = response.json()
                if error_response.get('message'):
                    error_description = error_response['message']
                    raise ConnectorError({'error_description': error_description})
                raise ConnectorError(error_response)
            else:
                try:
                    logger.error(response.json())
                    raise ConnectorError(str(response.json()))
                except Exception as err:
                    if isinstance(err, ConnectorError):
                        logger.error(str(response))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except requests.exceptions.JSONDecodeError:
            raise ConnectorError(
                'Error: {0}'.format(response.text if hasattr(response, 'text') and response.text else response))
        except Exception as err:
            raise ConnectorError(str(err))
        raise ConnectorError(response.text or response.reason)


def _check_health(config):
    try:
        bit_bucket = BitBucket(config)
        bit_bucket.make_request(endpoint=USERS_ENDPOINT + "/{0}".format(bit_bucket.username), validate_username=True)
        logger.info("BitBucket Connector Available")
        return True
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def handle_org_repo_name(params, is_pop=True):
    operation = params.pop if is_pop else params.get
    operation("repo_type", None)
    project_name = operation('org') if is_pop else operation('org')
    repo_name = operation('repo_name') if is_pop else operation('repo_name')
    return project_name, repo_name


def handle_comma_separated_input(_input):
    if isinstance(_input, (list, tuple)):
        return _input
    if isinstance(_input, str):
        return [i.strip() if isinstance(i, str) else i for i in _input.split(',')]
    return _input


def build_payload(params):
    if not params:
        return params
    result = dict()
    for k, v in params.items():
        if v or isinstance(v, (int, bool)):
            result[k] = v
    return result


def create_repository(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    payload = {
        "name": params.get("display_name"),
        "slug": params.get("name"),
        "scmId": SCM_ID,
        "project": {
            "key": params.get("org")
        },
        "links": params.get('links')
    }
    return bit_bucket.make_request(endpoint=REPOSITORY_ENDPOINT.format(params.get("org")), method='POST',
                                   data=json.dumps(payload))


def delete_repository(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    endpoint = REPOSITORY_ENDPOINT.format(params.get("org")) + '/' + params.get('repo_name')
    response = bit_bucket.make_request(endpoint=endpoint, method='DELETE')
    if response.status_code == 202:
        return response.json()
    raise ConnectorError("Error while deleting repository.")


def get_repository(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    endpoint = REPOSITORY_ENDPOINT.format(params.get("org")) + '/' + params.get('repo_name')
    return bit_bucket.make_request(endpoint=endpoint)


def get_file_from_repository(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = FILE_ENDPOINT.format(project_name, repo_name, params.pop("file_path"))
    return bit_bucket.make_request(endpoint=endpoint, params=params)


def create_update_file_contents(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = FILE_ENDPOINT.format(project_name, repo_name, params.pop("file_path"))
    files = {k: (None, v) for k, v in params.items() if not (v == "" or v is None)}
    headers = {
        'Authorization': "Bearer {0}".format(bit_bucket.api_key)
    }
    return bit_bucket.make_request(endpoint=endpoint, method='PUT', files=files, headers=headers)


def update_user_repository_permission(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_PERMISSION_ENDPOINT.format(project_name, repo_name)
    params['name'] = handle_comma_separated_input(params.get('name'))
    params['permission'] = "REPO_{0}".format(params.get('permission'))
    response = bit_bucket.make_request(endpoint=endpoint, method='PUT', params=params)
    return {"status_code": response.status_code,
            "message": "Permissions updated successfully."}


def get_users_with_repository_permission(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_PERMISSION_ENDPOINT.format(project_name, repo_name)
    return bit_bucket.make_request(endpoint=endpoint, params=params)


def create_repository_branch(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_BRANCH_ENDPOINT.format(project_name, repo_name)
    return bit_bucket.make_request(endpoint=endpoint, method='POST', data=json.dumps(params))


def find_repository_branches(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = FIND_BRANCHES_ENDPOINT.format(project_name, repo_name)
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=endpoint, params=payload)


def delete_repository_branch(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    find_branch_param = {
      "org": params.get('org'),
      "filterText": params.get('name'),
      "repo_name": params.get('repo_name'),
      "repo_type": params.get('repo_type'),
    }
    if not params.get('endPoint'):
        list_matching_branch = find_repository_branches(config, find_branch_param, *args, **kwargs)
        match_count = len(list_matching_branch.get('values', []))
        if match_count > 1:
            raise ConnectorError("Too many branches matched while guessing the endPoint, specify the endPoint to delete the branch.")
        elif match_count < 1:
            raise ConnectorError("No matching branch found to delete.")
        else:
            params['endPoint'] = list_matching_branch.get('values')[0].get('latestCommit')
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_BRANCH_ENDPOINT.format(project_name, repo_name)
    response = bit_bucket.make_request(endpoint=endpoint, method='DELETE', data=json.dumps(params))
    if response.status_code == 204:
        return {"status_code": 204, "message": "Branch deleted successfully."}
    try:
        response.raise_for_status()
        error_response = {"status_code": response.status_code, "error_message": response.text or response.reason}
        raise ConnectorError('Error while deleting the branch. {0}'.format(json.dumps(error_response, indent=4)))
    except Exception as err:
        raise ConnectorError(err)


def list_pull_request(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_PULL_REQUEST_ENDPOINT.format(project_name, repo_name)
    if params.get('pull_number'):
        endpoint += '/{0}'.format(params.get('pull_number'))
        return [bit_bucket.make_request(endpoint=endpoint)]
    if params.get('draft') == "" or params.get('draft') is None:
        params.pop('draft', None)
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=endpoint, params=payload)


def merge_pull_request(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_PULL_REQUEST_ENDPOINT.format(project_name, repo_name) + '/{0}/merge'.format(params.pop('pullRequestId'))
    version = params.pop('version') if params.get('version') else 0
    if params.get('strategyId'):
        params['strategyId'] = MERGE_STRATEGY_MAPPING.get(params.get('strategyId'), params.get('strategyId'))
    payload = build_payload(params)
    return bit_bucket.make_request(method="POST", endpoint=endpoint, params={"version": version}, data=json.dumps(payload))


def create_pull_request(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_PULL_REQUEST_ENDPOINT.format(project_name, repo_name)
    additional_fields = params.pop('additional_fields', None)
    reviewers = params.get('reviewers')
    if reviewers:
        reviewers = reviewers.split(',') if isinstance(reviewers, str) else reviewers
        reviewer_list = []
        for reviewer in reviewers:
            result = get_user(config, params={"username": reviewer.strip()})
            reviewer_list.append(result)
        params['reviewers'] = reviewer_list
    if additional_fields and isinstance(additional_fields, dict):
        params.update(additional_fields)
    for ref in ["fromRef", "toRef"]:
        branch_name = params.get(ref)
        payload = {
            "org": project_name,
            "order": "ALPHABETICAL",
            "repo_name": repo_name,
            "repo_type": "Organization",
            "filterText": branch_name,
            "boostMatches": True
        }
        data = find_repository_branches(config, payload)
        if data.get('size') == 0:
            raise ConnectorError("Invalid branch name '{0}' provided.".format(branch_name))
        else:
            for branch in data.get("values"):
                if branch_name == branch.get('displayId'):
                    params[ref] = branch
                    break
            else:
                raise ConnectorError("Branch name '{0}' not matched with any of the branches.".format(branch_name))
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=endpoint, method="POST", data=json.dumps(payload))


def create_pull_request_comment(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = PULL_REQUEST_COMMENT_ENDPOINT.format(project_name, repo_name, params.pop('id'))
    additional_fields = params.pop('additional_fields', None)
    if additional_fields and isinstance(additional_fields, dict):
        params.update(additional_fields)
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=endpoint, method="POST", data=json.dumps(payload))


def list_users(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=USERS_ENDPOINT, params=payload)


def get_user(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    return bit_bucket.make_request(endpoint=USERS_ENDPOINT + "/{0}".format(params.pop('username')))


def list_tags(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = TAGS_ENDPOINT.format(project_name, repo_name)
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=endpoint, params=payload)


def create_tag(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = CREATE_TAG_ENDPOINT.format(project_name, repo_name)
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=endpoint, method='POST', data=json.dumps(payload))


def list_pull_requests_comments(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    project_name, repo_name = handle_org_repo_name(params)
    endpoint = REPOSITORY_PULL_REQUEST_ENDPOINT.format(project_name, repo_name) + "/{0}/activities".format(params.pop('id'))
    payload = build_payload(params)
    return bit_bucket.make_request(endpoint=endpoint, params=payload)


def get_web_url(config, params, *args, **kwargs):
    bit_bucket = BitBucket(config)
    return {"server_url": bit_bucket.server_url}


def clone_repository(config, params, *args, **kwargs):
    try:
        bit_bucket = BitBucket(config)
        env = kwargs.get('env', {})
        archive_format = params.get('archive_format') if params.get('archive_format') else 'zip'
        url = bit_bucket.server_url + CLONE_ENDPOINT.format(params.get('org'), params.get('repo_name'))
        zip_file = '/tmp/bitbucket-{0}-{1}.{2}'.format(params.get('repo_name'), datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'), archive_format)
        branch_name = params.get('branch_name')
        branch_name_in_path = branch_name.replace('/', '-')
        CLONE_ACCEPT_HEADER = {
            "Authorization": "Bearer {0}".format(bit_bucket.api_key)
        }
        clone_params = {
            "format": archive_format,
            "at": "refs/heads/{0}".format(branch_name)
        }
        response = requests.request("GET", url, headers=CLONE_ACCEPT_HEADER, params=clone_params)
        if not response.ok:
            error_response = {
                "status_code": response.status_code,
                "message": response.reason if response.reason else response.text
            }
            raise ConnectorError("Error : {0}".format(error_response))
        with open(zip_file, "wb") as zipFile:
            zipFile.write(response.content)
        if params.get('clone_zip') is True:
            save_file_in_env(env, zip_file)
            return {"path": zip_file}
        else:
            unzip_file_path = os.path.join(settings.TMP_FILE_ROOT, "-".join((params.get('repo_name'), branch_name_in_path)))
            with ZipFile(zip_file, "r") as zip_ref:
                zip_ref.extractall(unzip_file_path)
            save_file_in_env(env, unzip_file_path)
            save_file_in_env(env, zip_file)
            return {"path": unzip_file_path}
    except ConnectorError as e:
        raise ConnectorError(e)
    except Exception as e:
        raise ConnectorError(e)


def _unzip_protected_file(file_iri=None, *args, **kwargs):
    try:
        env = kwargs.get('env', {})
        metadata = download_file_from_cyops(file_iri, None, *args, *args, **kwargs)
        file_name = metadata.get('cyops_file_path', None)
        source_filepath = os.path.join(settings.TMP_FILE_ROOT, file_name)
        target_filepath = os.path.join(settings.TMP_FILE_ROOT, datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))
        if os.path.exists(target_filepath):
            shutil.rmtree(target_filepath)
        with ZipFile(source_filepath) as zf:
            zipinfo = zf.infolist()
            for info in zipinfo:
                zf.extract(member=info, path=target_filepath)
        check_file_traversal(target_filepath)
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(target_filepath):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        save_file_in_env(env, target_filepath)
        save_file_in_env(env, file_name)
        return {"filenames": listOfFiles}
    except ConnectorError as e:
        raise ConnectorError(e)
    except Exception as e:
        raise ConnectorError(e)


def update_clone_repository(config, params, *args, **kwargs):
    try:
        env = kwargs.get('env', {})
        response = _unzip_protected_file(type='File IRI', file_iri=params.get('file_iri'), env=env)
        path = response['filenames'][0].split('/')
        root_src_dir = '/tmp/{0}/{1}/'.format(path[2], path[3])
        root_dst_dir = params.get('clone_path') + '/'
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    # in case of the src and dst are the same file
                    if os.path.samefile(src_file, dst_file):
                        continue
                    os.remove(dst_file)
                shutil.move(src_file, dst_dir)
        return {'status': 'finish'}
    except Exception as err:
        raise ConnectorError(err)


operations = {
    "create_repository": create_repository,
    "delete_repository": delete_repository,
    "get_file_from_repository": get_file_from_repository,
    "create_update_file_contents": create_update_file_contents,
    "update_user_repository_permission": update_user_repository_permission,
    "get_users_with_repository_permission": get_users_with_repository_permission,
    "find_repository_branches": find_repository_branches,
    "create_repository_branch": create_repository_branch,
    "delete_repository_branch": delete_repository_branch,
    "list_pull_request": list_pull_request,
    "list_pull_requests_comments": list_pull_requests_comments,
    "merge_pull_request": merge_pull_request,
    "create_pull_request": create_pull_request,
    "create_pull_request_comment": create_pull_request_comment,
    "list_tags": list_tags,
    "create_tag": create_tag,
    "get_web_url": get_web_url,
    "clone_repository": clone_repository,
    "update_clone_repository": update_clone_repository,
    "check_health": _check_health
}
