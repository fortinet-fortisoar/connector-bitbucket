# Edit the config_and_params.json file and add the necessary parameter values.
"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import os
import sys
import json
import pytest
import logging
import importlib
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
grandparent_directory = os.path.abspath(os.path.join(parent_directory, os.pardir))
sys.path.insert(0, str(grandparent_directory))

from connectors.core.connector import ConnectorError

with open('tests/config_and_params.json', 'r') as file:
    params = json.load(file)

module_name = 'bitbucket_1_0_0.operations'
conn_operations_module = importlib.import_module(module_name)
operations = conn_operations_module.operations

with open('info.json', 'r') as file:
    info_json = json.load(file)

logger = logging.getLogger(__name__)
    

# To test with different configuration values, adjust the index in the list below.
@pytest.fixture(scope="module")
def valid_credentials():
    return params.get('config')[0]
    
    
@pytest.fixture(scope="module")
def valid_credentials_with_token(valid_credentials):
    config = valid_credentials.copy()
    operations['check_health'](config)
    return config
    

@pytest.mark.checkhealth     
def test_check_health_success(valid_credentials):
    assert operations['check_health'](valid_credentials.copy())   
    

@pytest.mark.checkhealth     
def test_check_health_invalid_api_key(valid_credentials):
    invalid_creds = valid_credentials.copy()
    invalid_creds['api_key'] = params.get('invalid_params')['password']
    with pytest.raises(ConnectorError):
        assert operations['check_health'](invalid_creds)
    

@pytest.mark.checkhealth     
def test_check_health_invalid_server_url(valid_credentials):
    invalid_creds = valid_credentials.copy()
    invalid_creds['server_url'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['check_health'](invalid_creds)
    

@pytest.mark.checkhealth     
def test_check_health_invalid_username(valid_credentials):
    invalid_creds = valid_credentials.copy()
    invalid_creds['username'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['check_health'](invalid_creds)
    

@pytest.mark.create_repository
@pytest.mark.parametrize("input_params", params['create_repository'])
def test_create_repository_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['create_repository'](valid_credentials_with_token, input_params.copy())


@pytest.mark.delete_repository
@pytest.mark.parametrize("input_params", params['delete_repository'])
def test_delete_repository_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['delete_repository'](valid_credentials_with_token, input_params.copy())


# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.create_repository
@pytest.mark.schema_validation
def test_validate_create_repository_output_schema(valid_credentials_with_token):
    input_params = params.get('create_repository')[0].copy()
    input_params['name'] = 'test-repo'
    input_params['display_name'] = 'Test Repo'
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'create_repository':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['create_repository'](valid_credentials_with_token, input_params).keys() == schema.keys()
    

@pytest.mark.create_repository     
def test_create_repository_invalid_org(valid_credentials_with_token):
    input_params = params.get('create_repository')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_repository'](valid_credentials_with_token, input_params.copy())


@pytest.mark.delete_repository     
def test_delete_repository_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('delete_repository')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['delete_repository'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.delete_repository     
def test_delete_repository_invalid_org(valid_credentials_with_token):
    input_params = params.get('delete_repository')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['delete_repository'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_update_file_contents
@pytest.mark.parametrize("input_params", params['create_update_file_contents'])
def test_create_update_file_contents_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['create_update_file_contents'](valid_credentials_with_token, input_params.copy())


@pytest.mark.get_file_from_repository
@pytest.mark.parametrize("input_params", params['get_file_from_repository'])
def test_get_file_from_repository_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['get_file_from_repository'](valid_credentials_with_token, input_params.copy())
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.get_file_from_repository
@pytest.mark.schema_validation
def test_validate_get_file_from_repository_output_schema(valid_credentials_with_token):
    input_params = params.get('get_file_from_repository')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'get_file_from_repository':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['get_file_from_repository'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.get_file_from_repository     
def test_get_file_from_repository_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('get_file_from_repository')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    logger.error(f'params: {input_params}')
    with pytest.raises(ConnectorError):
        assert operations['get_file_from_repository'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.get_file_from_repository     
def test_get_file_from_repository_invalid_at(valid_credentials_with_token):
    input_params = params.get('get_file_from_repository')[0].copy()
    input_params['at'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['get_file_from_repository'](valid_credentials_with_token, input_params.copy()).get('values')
    

@pytest.mark.get_file_from_repository     
def test_get_file_from_repository_invalid_org(valid_credentials_with_token):
    input_params = params.get('get_file_from_repository')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['get_file_from_repository'](valid_credentials_with_token, input_params.copy())

    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.create_update_file_contents
@pytest.mark.schema_validation
def test_validate_create_update_file_contents_output_schema(valid_credentials_with_token):
    input_params = params.get('create_update_file_contents')[0].copy()
    input_params['file_path'] = 'test.py'
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'create_update_file_contents':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['create_update_file_contents'](valid_credentials_with_token, input_params).keys() == schema.keys()
    

@pytest.mark.create_update_file_contents     
def test_create_update_file_contents_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('create_update_file_contents')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_update_file_contents'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_update_file_contents     
def test_create_update_file_contents_invalid_sourceCommitId(valid_credentials_with_token):
    input_params = params.get('create_update_file_contents')[0].copy()
    input_params['sourceCommitId'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_update_file_contents'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_update_file_contents     
def test_create_update_file_contents_invalid_sourceBranch(valid_credentials_with_token):
    input_params = params.get('create_update_file_contents')[0].copy()
    input_params['sourceBranch'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_update_file_contents'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_update_file_contents     
def test_create_update_file_contents_invalid_org(valid_credentials_with_token):
    input_params = params.get('create_update_file_contents')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_update_file_contents'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_update_file_contents     
def test_create_update_file_contents_invalid_branch(valid_credentials_with_token):
    input_params = params.get('create_update_file_contents')[0].copy()
    input_params['branch'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_update_file_contents'](valid_credentials_with_token, input_params.copy())


@pytest.mark.update_user_repository_permission
@pytest.mark.parametrize("input_params", params['update_user_repository_permission'])
def test_update_user_repository_permission_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['update_user_repository_permission'](valid_credentials_with_token, input_params.copy())
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.update_user_repository_permission
@pytest.mark.schema_validation
def test_validate_update_user_repository_permission_output_schema(valid_credentials_with_token):
    input_params = params.get('update_user_repository_permission')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'update_user_repository_permission':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['update_user_repository_permission'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.update_user_repository_permission     
def test_update_user_repository_permission_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('update_user_repository_permission')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['update_user_repository_permission'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.update_user_repository_permission     
def test_update_user_repository_permission_invalid_name(valid_credentials_with_token):
    input_params = params.get('update_user_repository_permission')[0].copy()
    input_params['name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['update_user_repository_permission'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.update_user_repository_permission     
def test_update_user_repository_permission_invalid_org(valid_credentials_with_token):
    input_params = params.get('update_user_repository_permission')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['update_user_repository_permission'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.get_users_with_repository_permission
@pytest.mark.parametrize("input_params", params['get_users_with_repository_permission'])
def test_get_users_with_repository_permission_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['get_users_with_repository_permission'](valid_credentials_with_token, input_params.copy())
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.get_users_with_repository_permission
@pytest.mark.schema_validation
def test_validate_get_users_with_repository_permission_output_schema(valid_credentials_with_token):
    input_params = params.get('get_users_with_repository_permission')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'get_users_with_repository_permission':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['get_users_with_repository_permission'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.get_users_with_repository_permission     
def test_get_users_with_repository_permission_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('get_users_with_repository_permission')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['get_users_with_repository_permission'](valid_credentials_with_token, input_params.copy())


@pytest.mark.get_users_with_repository_permission     
def test_get_users_with_repository_permission_invalid_filter(valid_credentials_with_token):
    input_params = params.get('get_users_with_repository_permission')[0].copy()
    input_params['filter'] = params.get('invalid_params')['text']
    result = operations['get_users_with_repository_permission'](valid_credentials_with_token, input_params.copy())
    assert not result.get('values')
    

@pytest.mark.get_users_with_repository_permission     
def test_get_users_with_repository_permission_invalid_org(valid_credentials_with_token):
    input_params = params.get('get_users_with_repository_permission')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['get_users_with_repository_permission'](valid_credentials_with_token, input_params.copy())


@pytest.mark.find_repository_branches
@pytest.mark.parametrize("input_params", params['find_repository_branches'])
def test_find_repository_branches_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['find_repository_branches'](valid_credentials_with_token, input_params.copy())

    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.find_repository_branches
@pytest.mark.schema_validation
def test_validate_find_repository_branches_output_schema(valid_credentials_with_token):
    input_params = params.get('find_repository_branches')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'find_repository_branches':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['find_repository_branches'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.find_repository_branches     
def test_find_repository_branches_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('find_repository_branches')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['find_repository_branches'](valid_credentials_with_token, input_params.copy())


@pytest.mark.find_repository_branches     
def test_find_repository_branches_invalid_filterText(valid_credentials_with_token):
    input_params = params.get('find_repository_branches')[0].copy()
    input_params['filterText'] = params.get('invalid_params')['text']
    assert not operations['find_repository_branches'](valid_credentials_with_token, input_params.copy()).get('values')
    

@pytest.mark.find_repository_branches     
def test_find_repository_branches_invalid_org(valid_credentials_with_token):
    input_params = params.get('find_repository_branches')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['find_repository_branches'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_repository_branch
@pytest.mark.parametrize("input_params", params['create_repository_branch'])
def test_create_repository_branch_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['create_repository_branch'](valid_credentials_with_token, input_params.copy())


# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.create_repository_branch
@pytest.mark.schema_validation
def test_validate_create_repository_branch_output_schema(valid_credentials_with_token):
    input_params = params.get('create_repository_branch')[0].copy()
    input_params['name'] = 'output_schema'
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'create_repository_branch':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['create_repository_branch'](valid_credentials_with_token, input_params).keys() == schema.keys()
    

@pytest.mark.create_repository_branch     
def test_create_repository_branch_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('create_repository_branch')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_repository_branch'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_repository_branch     
def test_create_repository_branch_invalid_name(valid_credentials_with_token):
    input_params = params.get('create_repository_branch')[0].copy()
    input_params['name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_repository_branch'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_repository_branch     
def test_create_repository_branch_invalid_startPoint(valid_credentials_with_token):
    input_params = params.get('create_repository_branch')[0].copy()
    input_params['startPoint'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_repository_branch'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_repository_branch     
def test_create_repository_branch_invalid_org(valid_credentials_with_token):
    input_params = params.get('create_repository_branch')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_repository_branch'](valid_credentials_with_token, input_params.copy())


@pytest.mark.delete_repository_branch
def test_delete_repository_branch_invalid_endPoint(valid_credentials_with_token):
    input_params = params.get('delete_repository_branch')[0].copy()
    input_params['endPoint'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['delete_repository_branch'](valid_credentials_with_token, input_params.copy())


# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.delete_repository_branch
@pytest.mark.schema_validation
def test_validate_delete_repository_branch_output_schema(valid_credentials_with_token):
    input_params = params.get('delete_repository_branch')[0].copy()
    input_params['name'] = 'output_schema'
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'delete_repository_branch':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['delete_repository_branch'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()


@pytest.mark.delete_repository_branch
def test_delete_repository_branch_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('delete_repository_branch')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['delete_repository_branch'](valid_credentials_with_token, input_params.copy())


@pytest.mark.delete_repository_branch
def test_delete_repository_branch_invalid_name(valid_credentials_with_token):
    input_params = params.get('delete_repository_branch')[0].copy()
    input_params['name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['delete_repository_branch'](valid_credentials_with_token, input_params.copy())


@pytest.mark.delete_repository_branch
def test_delete_repository_branch_invalid_org(valid_credentials_with_token):
    input_params = params.get('delete_repository_branch')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['delete_repository_branch'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_pull_request
@pytest.mark.parametrize("input_params", params['create_pull_request'])
@pytest.mark.schema_validation
def test_create_pull_request_success(valid_credentials_with_token, input_params):
    create_file_params = params['create_update_file_contents'][0].copy()
    create_file_params['file_path'] = 'new_file_for_pr1.txt'
    create_file_params['branch'] = 'develop'
    test_create_update_file_contents_success(valid_credentials_with_token, create_file_params)
    logger.info("params: {0}".format(input_params))
    result = operations['create_pull_request'](valid_credentials_with_token, input_params.copy())
    assert result
    params['merge_pull_request'][0]['pullRequestId'] = result.get('id')
    params['create_pull_request_comment'][0]['id'] = result.get('id')
    params['list_pull_requests_comments'][0]['id'] = result.get('id')
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'create_pull_request':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert set(result.keys()) == set(schema.keys())


@pytest.mark.create_pull_request
def test_create_pull_request_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('create_pull_request')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_pull_request
def test_create_pull_request_invalid_toRef(valid_credentials_with_token):
    input_params = params.get('create_pull_request')[0].copy()
    input_params['toRef'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_pull_request
def test_create_pull_request_invalid_reviewers(valid_credentials_with_token):
    input_params = params.get('create_pull_request')[0].copy()
    input_params['reviewers'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_pull_request
def test_create_pull_request_invalid_fromRef(valid_credentials_with_token):
    input_params = params.get('create_pull_request')[0].copy()
    input_params['fromRef'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_pull_request
def test_create_pull_request_invalid_org(valid_credentials_with_token):
    input_params = params.get('create_pull_request')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request'](valid_credentials_with_token, input_params.copy())


@pytest.mark.list_pull_request
@pytest.mark.parametrize("input_params", params['list_pull_request'])
def test_list_pull_request_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['list_pull_request'](valid_credentials_with_token, input_params.copy())
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.list_pull_request
@pytest.mark.schema_validation
def test_validate_list_pull_request_output_schema(valid_credentials_with_token):
    input_params = params.get('list_pull_request')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'list_pull_request':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert set(operations['list_pull_request'](valid_credentials_with_token, input_params.copy()).keys()) == set(schema.keys())
    

@pytest.mark.list_pull_request     
def test_list_pull_request_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('list_pull_request')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_pull_request'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.list_pull_request     
def test_list_pull_request_invalid_filterText(valid_credentials_with_token):
    input_params = params.get('list_pull_request')[0].copy()
    input_params['filterText'] = params.get('invalid_params')['text']
    assert not operations['list_pull_request'](valid_credentials_with_token, input_params.copy()).get('values')


@pytest.mark.list_pull_request     
def test_list_pull_request_invalid_at(valid_credentials_with_token):
    input_params = params.get('list_pull_request')[0].copy()
    input_params['at'] = params.get('invalid_params')['text']
    assert not operations['list_pull_request'](valid_credentials_with_token, input_params.copy()).get('values')
    

@pytest.mark.list_pull_request     
def test_list_pull_request_invalid_org(valid_credentials_with_token):
    input_params = params.get('list_pull_request')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_pull_request'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.list_pull_request     
def test_list_pull_request_invalid_pull_number(valid_credentials_with_token):
    input_params = params.get('list_pull_request')[0].copy()
    input_params['pull_number'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_pull_request'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.merge_pull_request
@pytest.mark.schema_validation
@pytest.mark.parametrize("input_params", params['merge_pull_request'])
def test_merge_pull_request_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    result = operations['merge_pull_request'](valid_credentials_with_token, input_params.copy())
    assert result
    logger.error("test_merge_pull_request_success: \n{}".format(result))
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'merge_pull_request':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert set(result.keys()) == set(schema.keys())


@pytest.mark.merge_pull_request     
def test_merge_pull_request_invalid_version(valid_credentials_with_token):
    input_params = params.get('merge_pull_request')[0].copy()
    input_params['version'] = params.get('invalid_params')['integer']
    with pytest.raises(ConnectorError):
        assert operations['merge_pull_request'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.merge_pull_request     
def test_merge_pull_request_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('merge_pull_request')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['merge_pull_request'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.merge_pull_request     
def test_merge_pull_request_invalid_pullRequestId(valid_credentials_with_token):
    input_params = params.get('merge_pull_request')[0].copy()
    input_params['pullRequestId'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['merge_pull_request'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.merge_pull_request     
def test_merge_pull_request_invalid_org(valid_credentials_with_token):
    input_params = params.get('merge_pull_request')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['merge_pull_request'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_pull_request_comment
@pytest.mark.parametrize("input_params", params['create_pull_request_comment'])
def test_create_pull_request_comment_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['create_pull_request_comment'](valid_credentials_with_token, input_params.copy())


# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.create_pull_request_comment
@pytest.mark.schema_validation
def test_validate_create_pull_request_comment_output_schema(valid_credentials_with_token):
    input_params = params.get('create_pull_request_comment')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'create_pull_request_comment':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['create_pull_request_comment'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()


@pytest.mark.create_pull_request_comment     
def test_create_pull_request_comment_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('create_pull_request_comment')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request_comment'](valid_credentials_with_token, input_params.copy())


@pytest.mark.create_pull_request_comment     
def test_create_pull_request_comment_invalid_id(valid_credentials_with_token):
    input_params = params.get('create_pull_request_comment')[0].copy()
    input_params['id'] = params.get('invalid_params')['integer']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request_comment'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_pull_request_comment     
def test_create_pull_request_comment_invalid_org(valid_credentials_with_token):
    input_params = params.get('create_pull_request_comment')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_pull_request_comment'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.list_tags
@pytest.mark.parametrize("input_params", params['list_tags'])
def test_list_tags_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['list_tags'](valid_credentials_with_token, input_params.copy())
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.list_tags
@pytest.mark.schema_validation
def test_validate_list_tags_output_schema(valid_credentials_with_token):
    input_params = params.get('list_tags')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'list_tags':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['list_tags'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.list_tags     
def test_list_tags_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('list_tags')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_tags'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.list_tags     
def test_list_tags_invalid_filterText(valid_credentials_with_token):
    input_params = params.get('list_tags')[0].copy()
    input_params['filterText'] = params.get('invalid_params')['text']
    assert not operations['list_tags'](valid_credentials_with_token, input_params.copy()).get('values')


@pytest.mark.list_tags     
def test_list_tags_invalid_org(valid_credentials_with_token):
    input_params = params.get('list_tags')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_tags'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_tag
@pytest.mark.parametrize("input_params", params['create_tag'])
def test_create_tag_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['create_tag'](valid_credentials_with_token, input_params.copy())
    input_params['name'] = 'tag-output-schema'
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.create_tag
@pytest.mark.schema_validation
def test_validate_create_tag_output_schema(valid_credentials_with_token):
    input_params = params.get('create_tag')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'create_tag':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['create_tag'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.create_tag     
def test_create_tag_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('create_tag')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_tag'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_tag     
def test_create_tag_invalid_name(valid_credentials_with_token):
    input_params = params.get('create_tag')[0].copy()
    input_params['name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_tag'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_tag     
def test_create_tag_invalid_startPoint(valid_credentials_with_token):
    input_params = params.get('create_tag')[0].copy()
    input_params['startPoint'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_tag'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.create_tag     
def test_create_tag_invalid_org(valid_credentials_with_token):
    input_params = params.get('create_tag')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['create_tag'](valid_credentials_with_token, input_params.copy())


@pytest.mark.get_web_url
@pytest.mark.parametrize("input_params", params['get_web_url'])
def test_get_web_url_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['get_web_url'](valid_credentials_with_token, input_params.copy())
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.get_web_url
@pytest.mark.schema_validation
def test_validate_get_web_url_output_schema(valid_credentials_with_token):
    input_params = params.get('get_web_url')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'get_web_url':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['get_web_url'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.list_pull_requests_comments
@pytest.mark.parametrize("input_params", params['list_pull_requests_comments'])
def test_list_pull_requests_comments_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['list_pull_requests_comments'](valid_credentials_with_token, input_params.copy())
  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.list_pull_requests_comments
@pytest.mark.schema_validation
def test_validate_list_pull_requests_comments_output_schema(valid_credentials_with_token):
    input_params = params.get('list_pull_requests_comments')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'list_pull_requests_comments':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['list_pull_requests_comments'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.list_pull_requests_comments     
def test_list_pull_requests_comments_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('list_pull_requests_comments')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_pull_requests_comments'](valid_credentials_with_token, input_params.copy())


@pytest.mark.list_pull_requests_comments     
def test_list_pull_requests_comments_invalid_id(valid_credentials_with_token):
    input_params = params.get('list_pull_requests_comments')[0].copy()
    input_params['id'] = params.get('invalid_params')['integer']
    with pytest.raises(ConnectorError):
        assert operations['list_pull_requests_comments'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.list_pull_requests_comments     
def test_list_pull_requests_comments_invalid_org(valid_credentials_with_token):
    input_params = params.get('list_pull_requests_comments')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_pull_requests_comments'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.list_pull_requests_comments     
def test_list_pull_requests_comments_invalid_fromId(valid_credentials_with_token):
    input_params = params.get('list_pull_requests_comments')[0].copy()
    input_params['fromId'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['list_pull_requests_comments'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.clone_repository
@pytest.mark.parametrize("input_params", params['clone_repository'])
def test_clone_repository_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    result = operations['clone_repository'](valid_credentials_with_token, input_params.copy())
    logger.error(f'xclone: {result}')
    params['update_clone_repository'][0]['clone_path'] = result.get('path')
    assert result

  
    
# Ensure that the provided input_params yield the correct output schema, or adjust the index in the list below.
# conditional_output_schema not supported.
@pytest.mark.clone_repository
@pytest.mark.schema_validation
def test_validate_clone_repository_output_schema(valid_credentials_with_token):
    input_params = params.get('clone_repository')[0]
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'clone_repository':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['clone_repository'](valid_credentials_with_token, input_params.copy()).keys() == schema.keys()
    

@pytest.mark.clone_repository     
def test_clone_repository_invalid_repo_name(valid_credentials_with_token):
    input_params = params.get('clone_repository')[0].copy()
    input_params['repo_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['clone_repository'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.clone_repository     
def test_clone_repository_invalid_org(valid_credentials_with_token):
    input_params = params.get('clone_repository')[0].copy()
    input_params['org'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['clone_repository'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.clone_repository     
def test_clone_repository_invalid_branch_name(valid_credentials_with_token):
    input_params = params.get('clone_repository')[0].copy()
    input_params['branch_name'] = params.get('invalid_params')['text']
    with pytest.raises(ConnectorError):
        assert operations['clone_repository'](valid_credentials_with_token, input_params.copy())
    

@pytest.mark.delete_repository_branch
@pytest.mark.parametrize("input_params", params['delete_repository_branch'])
def test_delete_repository_branch_success(valid_credentials_with_token, input_params):
    logger.info("params: {0}".format(input_params))
    assert operations['delete_repository_branch'](valid_credentials_with_token, input_params.copy())


@pytest.mark.delete_repository
@pytest.mark.schema_validation
def test_validate_delete_repository_output_schema(valid_credentials_with_token):
    input_params = params.get('delete_repository')[0].copy()
    input_params['repo_name'] = 'test-repo'
    schema = {}
    for operation in info_json.get("operations"):
        if operation.get('operation') == 'delete_repository':
            if operation.get('conditional_output_schema'):
                schema = {}
            else:
                schema = operation.get('output_schema')
            break
    logger.info("output_schema: {0}".format(schema))
    assert operations['delete_repository'](valid_credentials_with_token, input_params).keys() == schema.keys()
