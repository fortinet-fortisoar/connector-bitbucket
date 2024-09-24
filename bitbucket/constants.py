"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

SCM_ID = "git"
REPOSITORY_ENDPOINT = "/rest/api/latest/projects/{0}/repos"
FILE_ENDPOINT = "/rest/api/latest/projects/{0}/repos/{1}/browse/{2}"
REPOSITORY_PERMISSION_ENDPOINT = '/rest/api/latest/projects/{0}/repos/{1}/permissions/users'
REPOSITORY_BRANCH_ENDPOINT = '/rest/branch-utils/latest/projects/{0}/repos/{1}/branches'
FIND_BRANCHES_ENDPOINT = '/rest/api/latest/projects/{0}/repos/{1}/branches?'
REPOSITORY_PULL_REQUEST_ENDPOINT = '/rest/api/latest/projects/{0}/repos/{1}/pull-requests'
PULL_REQUEST_COMMENT_ENDPOINT = '/rest/api/latest/projects/{0}/repos/{1}/pull-requests/{2}/comments'
USERS_ENDPOINT = '/rest/api/latest/users'
TAGS_ENDPOINT = '/rest/api/latest/projects/{0}/repos/{1}/tags'
CREATE_TAG_ENDPOINT = '/rest/git/latest/projects/{0}/repos/{1}/tags'

MERGE_STRATEGY_MAPPING = {
    "Merge Commit": "no-ff",
    "Fast-forward": "ff",
    "Fast-forward only": "ff-only",
    "Rebase and merge": "rebase-no-ff",
    "Rebase and fast-forward": "rebase-ff-only",
    "Squash": "squash",
    "Squash, fast-forward only": "squash-ff-only"
}

CLONE_ENDPOINT = '/rest/api/latest/projects/{0}/repos/{1}/archive'
