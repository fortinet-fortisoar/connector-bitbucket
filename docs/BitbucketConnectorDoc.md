## About the connector
Bitbucket is a comprehensive platform designed to streamline the software development process. It encompasses all aspects of the development lifecycle, offering seamless integration and efficiency throughout the journey from initial project planning to deployment and beyond. With Bitbucket, teams can seamlessly manage their source code, facilitate collaboration, and ensure the quality and security of their software.
<p>This document provides information about the Bitbucket Connector, which facilitates automated interactions, with a Bitbucket server using FortiSOAR&trade; playbooks. Add the Bitbucket Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Bitbucket.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-bitbucket</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Bitbucket server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Bitbucket server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Bitbucket</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the IP address or hostname of the Bitbucket server to which you will connect and perform automated operations.
</td>
</tr><tr><td>Port</td><td>Specify the port of the Bitbucket server to connect and perform automated operations. By default, it is set, 443.
</td>
</tr><tr><td>Username</td><td>Specify the username used to access the Bitbucket server to connect and perform the automated operations.
</td>
</tr><tr><td>Access Token</td><td>Specify the access token that is provided to you by a Bitbucket administrator that you will use to access the Bitbucket REST API. For information on generating access tokens, refer .
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks, and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Repository</td><td>Creates a new repository based on the repository type, repository name, and other input parameters that you have specified.</td><td>create_repository <br/>Investigation</td></tr>
<tr><td>Delete Repository</td><td>Deletes a repository including all associated resources, like issues and pull requests, based on the repository type, repository name, and other input parameters that you have specified.</td><td>delete_repository <br/>Investigation</td></tr>
<tr><td>Get File Details</td><td>Retrieves information such as name, size, content, etc. about a file from the Bitbucket repository based on the repository ID, branch name, file name, and other input parameters that you have specified.</td><td>get_file_from_repository <br/>Investigation</td></tr>
<tr><td>Create or Update File Contents</td><td>Creates or updates a single file in the Bitbucket repository based on the repository ID, branch name, file name and other input parameters.</td><td>update_file_in_repository <br/>Investigation</td></tr>
<tr><td>Update User Repository Permission</td><td>Updates(promote or demote) a user's permission levels for specified repository.</td><td>update_user_repository_permission <br/>Investigation</td></tr>
<tr><td>Get Member List of Repository</td><td>Retrieves a list of group or repository members viewable by the authenticated user, including inherited members, invited users, and permissions through ancestor groups.</td><td>get_users_with_repository_permission <br/>Investigation</td></tr>
<tr><td>Get Repository Branch List</td><td>Lists repository branches for the specified repository on Bitbucket based on the repository type, organization or repository owner's name, repository name, and other input parameters you have specified</td><td>find_repository_branches <br/>Investigation</td></tr>
<tr><td>Create Repository Branch</td><td>Creates a new branch in the repository based on the repository type, branch name, and other input parameters that you have specified.</td><td>create_repository_branch <br/>Investigation</td></tr>
<tr><td>Delete Repository Branch</td><td>Deletes a branch from the repository based on the repository type and branch name that you have specified.</td><td>delete_repository_branch <br/>Investigation</td></tr>
<tr><td>Get Pull Request List</td><td>Lists pull requests for the specified repository on Bitbucket based on the repository type, organization or repository owner's name, repository name, and other input parameters you have specified</td><td>list_pull_request <br/>Investigation</td></tr>
<tr><td>Merge Pull Request</td><td>Accept and merge changes in the pull request based on the repository type, repository name, and other input parameters that you have specified.</td><td>merge_pull_request <br/>Investigation</td></tr>
<tr><td>Create Pull Request</td><td>Creates a pull request for the specified repository on Bitbucket based on the repository type, organization or repository owner's name, repository name, and other input parameters you have specified</td><td>create_pull_request <br/>Investigation</td></tr>
<tr><td>Create Pull Request Comment</td><td>Creates a new note/comment on a pull request based on the repository type, repository name, and other input parameters that you have specified.</td><td>create_pull_request_comment <br/>Investigation</td></tr>
<tr><td>Get Tag List</td><td>Retrieves a paginated list of tags, sorted by the date when they were released, based on the repository type, repository name, and other input parameters that you have specified.</td><td>list_releases <br/>Investigation</td></tr>
<tr><td>Create Tag</td><td>Creates a new Bitbucket tag based on the repository type, repository name, and other input parameters that you have specified. Developer level access to the repository is required to create a tag.</td><td>create_tag <br/>Investigation</td></tr>
<tr><td>Get Server URL</td><td>Retrieves the server URL (Web URL) of the configured Bitbucket server.</td><td>get_web_url <br/>Investigation</td></tr>
<tr><td>Get Pull Request Comments</td><td>Retrieves a list of all comments for a pull request based on the repository type, repository name, and other input parameters that you have specified.</td><td>list_pull_request_comments <br/>Investigation</td></tr>
<tr><td>Clone Repository</td><td>Clones the specified repository in a Bitbucket project based on the repository type, repository name, and other input parameters that you have specified.</td><td>clone_repository <br/>Investigation</td></tr>
<tr><td>Update Remote Repository</td><td>Applies changes made in a FortiSOAR file to the specified remote repository that is cloned from Bitbucket based on the file IRI and cloned repository path you have specified</td><td>update_remote_repository <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Repository
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository to create on Bitbucket. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, within which to create the repository.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository to create.
</td></tr><tr><td>Repository Display Name</td><td>Specify the name of the repository to create.
</td></tr><tr><td>Links</td><td>(Optional) Specify links in the JSON format
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "slug": "",
    "id": "",
    "name": "",
    "hierarchyId": "",
    "scmId": "",
    "state": "",
    "statusMessage": "",
    "forkable": "",
    "project": {
        "key": "",
        "id": "",
        "name": "",
        "description": "",
        "public": "",
        "type": "",
        "links": {
            "self": [
                {
                    "href": ""
                }
            ]
        }
    },
    "public": "",
    "archived": "",
    "links": {
        "clone": [
            {
                "href": "",
                "name": ""
            }
        ],
        "self": [
            {
                "href": ""
            }
        ]
    }
}</pre>

### operation: Delete Repository
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository to delete on Bitbucket. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, within which to delete the repository.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, whose repository is to be deleted.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository to delete.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "context": "",
    "message": "",
    "exceptionName": ""
}</pre>

### operation: Get File Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository from which to retrieve the file. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, within whose repository the file is to be retrieved.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, within whose repository the file is to be retrieved.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository from which the file is to be retrieved.
</td></tr><tr><td>Branch Name</td><td>Specify the name of the branch from which to retrieve the file.
</td></tr><tr><td>File Name</td><td>Specify the name of the file to retrieve.
</td></tr><tr><td>Size</td><td>Select to retrieve only file size. File content will not be retrieved. By default is is set to false
<br><strong>If you choose 'false'</strong><ul><li>Type: Select to retrieve only type of file in the response. File content will not be retrieved. By default, it is set to false</li><strong>If you choose 'false'</strong><ul><li>Blame: Select to retrieve blame in the response. By default, it is set to false</li></ul></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "size": "",
    "limit": "",
    "lines": [
        {
            "text": ""
        }
    ],
    "start": "",
    "isLastPage": "",
    "nextPageStart": ""
}</pre>

### operation: Create or Update File Contents
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository in which to created/updated the file. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, within whose repository the file is to be created/updated..</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, within whose repository the file is to be updated.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository in which the file is to be created/updated.
</td></tr><tr><td>File Name</td><td>Specify the name of the file to created/updatedcreated/updated.
</td></tr><tr><td>Branch Name</td><td>Specify the name of the branch in which to created/updated the file.
</td></tr><tr><td>Content Information</td><td>Specify the contents to update in the file being created/updated.
</td></tr><tr><td>Commit Message</td><td>Specify the commit message for creating/updating the file.
</td></tr><tr><td>Source Branch</td><td>Specify the starting point for branch. If provided and different from "Branch Name", branch will be created as a new branch, branching off from "Source Branch".
</td></tr><tr><td>Source Commit ID</td><td>Specify the commit ID of the file before it was edited, used to identify if content has changed. Note: Do not specify this field if to create new file.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "author": {
        "id": "",
        "name": "",
        "slug": "",
        "type": "",
        "links": {
            "self": [
                {
                    "href": ""
                }
            ]
        },
        "active": "",
        "displayName": "",
        "emailAddress": ""
    },
    "message": "",
    "parents": [],
    "committer": {
        "id": "",
        "name": "",
        "slug": "",
        "type": "",
        "links": {
            "self": [
                {
                    "href": ""
                }
            ]
        },
        "active": "",
        "displayName": "",
        "emailAddress": ""
    },
    "displayId": "",
    "authorTimestamp": "",
    "committerTimestamp": ""
}</pre>

### operation: Update User Repository Permission
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the repository type, using which you want to update the user permissions.
You can choose from Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization of the repository on Bitbucket whose user permissions is to be updated.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the account holder of the repository on Bitbucket whose user permissions is to be updated.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository on Bitbucket whose user permissions is to be updated.
</td></tr><tr><td>Usernames</td><td>Specify the comma separated usernames of the user's whose repository permissions are to be updated.
</td></tr><tr><td>REPOSITORY Permissions</td><td>Select the access level to grant to the specified collaborator. You can select from following options: No access , Minimal access ,Guest ,Reporter ,Developer , Maintainer. NOTE: Permissions are applicable only on organization-owned repositories.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "status_code": ""
}</pre>

### operation: Get Member List of Repository
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository to retrieve its collaborators. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, from which to retrieve the collaborators.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, from which to retrieve the collaborators.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository from which to retrieve the collaborators.
</td></tr><tr><td>Filter</td><td>Specify a string to filter user names. Only user names containing this string will be returned.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to return the results of the operation.
</td></tr><tr><td>Per Page</td><td>(Optional) Specify the number of results, per page, that this operation should return.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "size": "",
    "limit": "",
    "start": "",
    "values": [
        {
            "user": {
                "id": "",
                "name": "",
                "slug": "",
                "type": "",
                "links": {
                    "self": [
                        {
                            "href": ""
                        }
                    ]
                },
                "active": "",
                "displayName": "",
                "emailAddress": ""
            },
            "permission": ""
        }
    ],
    "isLastPage": ""
}</pre>

### operation: Get Repository Branch List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository whose, branches are to be retrieved from Bitbucket. You can choose from Organization or User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, whose repository's branches are to be retrieved, in the Organization Name field.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, whose repository's branches are to be retrieved, in the Repository Owner field.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository whose branches are to be retrieved from Bitbucket.
</td></tr><tr><td>Filter Text</td><td>(Optional) Specify the text to filter retrieve branches contains the supplied string in name.
</td></tr><tr><td>Boost Matches to Top</td><td>(Optional) Specify whether to exact and prefix matches boost to the top of the search results. By default set to false.
</td></tr><tr><td>Retrieve Metadata</td><td>(Optional) Specify whether to retrieve plugin-provided metadata about each branch or not. By default set to false.
</td></tr><tr><td>Sort Order</td><td>(Optional) Select the order to sort the results returned by this operation. You can choose from the following options: ALPHABETICAL or MODIFICATION
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which you want the operation to return the results of the operation.
</td></tr><tr><td>Per Page</td><td>(Optional) Specify the number of results, per page, that this operation should return.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "size": "",
    "limit": "",
    "start": "",
    "values": [
        {
            "id": "",
            "type": "",
            "displayId": "",
            "isDefault": "",
            "latestCommit": "",
            "latestChangeset": ""
        }
    ],
    "isLastPage": ""
}</pre>

### operation: Create Repository Branch
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository in which to create the branch. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, in which to create the branch.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, in which to create the branch.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository in which to create the branch.
</td></tr><tr><td>Branch Name</td><td>Specify the name of the branch to create.
</td></tr><tr><td>Reference Branch</td><td>Specify the branch name or the commit ID from which to create the new branch.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "type": "",
    "displayId": "",
    "isDefault": "",
    "latestCommit": "",
    "latestChangeset": ""
}</pre>

### operation: Delete Repository Branch
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository in which to delete the branch. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, in which to delete the branch.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, in which to delete the branch.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository in which to delete the branch.
</td></tr><tr><td>Branch</td><td>Specify the name of the branch to delete.
</td></tr><tr><td>End Point</td><td>Specify commit ID that the provided branch is expected to point to.
</td></tr><tr><td>Dry Run</td><td>Check to do just a dry run, Don't actually delete the branch.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status_code": "",
    "message": ""
}</pre>

### operation: Get Pull Request List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository whose, pull requests are to be retrieved from Bitbucket. You can choose from Organization or User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, whose repository's pull requests are to be retrieved, in the Organization Name field.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, whose repository's pull requests are to be retrieved, in the Repository Owner field.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository whose pull requests are to be retrieved from Bitbucket.
</td></tr><tr><td>Pull Number</td><td>(Optional) Specify the ID of the pull request which is to be retrieved.
</td></tr><tr><td>Filter Text</td><td>(Optional) Specify the text to filter retrieve pull requests contains the supplied string in title or description.
</td></tr><tr><td>State</td><td>(Optional) Select the state of the pull requests whose details you want to retrieve from Bitbucket. The state parameter filters the results returned by this operation to only pull requests that match the selected state. You can choose between All, Open, DECLINED or MERGED.
</td></tr><tr><td>Direction</td><td>(Optional) Select the direction relative to the specified repository. You can choose from the following options: INCOMING or OUTGOING
<br><strong>If you choose 'INCOMING'</strong><ul><li>Target Branch: (Optional) Specify the fully-qualified branch ID of the target branch to filter the results returned by this operation to only pull requests that match the specified target branch name.</li></ul><strong>If you choose 'OUTGOING'</strong><ul><li>Source Branch: (Optional) Specify the fully-qualified branch ID of the source branch to filter the results returned by this operation to only pull requests that match the specified source branch name.</li></ul></td></tr><tr><td>With Attributes</td><td>whether to return additional pull request attributes.
</td></tr><tr><td>With Properties</td><td>whether to return additional pull request properties.
</td></tr><tr><td>Draft</td><td>Specify draft status of pull requests to be retrieved.
</td></tr><tr><td>Sort Order</td><td>(Optional) Select the order to sort the results returned by this operation. You can choose from the following options: NEWEST or OLDEST
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which you want the operation to return the results of the operation.
</td></tr><tr><td>Per Page</td><td>(Optional) Specify the number of results, per page, that this operation should return.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "size": "",
    "limit": "",
    "isLastPage": "",
    "values": [
        {
            "id": "",
            "version": "",
            "title": "",
            "state": "",
            "open": "",
            "closed": "",
            "draft": "",
            "createdDate": "",
            "updatedDate": "",
            "fromRef": {
                "id": "",
                "displayId": "",
                "latestCommit": "",
                "type": "",
                "repository": {
                    "slug": "",
                    "id": "",
                    "name": "",
                    "hierarchyId": "",
                    "scmId": "",
                    "state": "",
                    "statusMessage": "",
                    "forkable": "",
                    "project": {
                        "key": "",
                        "id": "",
                        "name": "",
                        "public": "",
                        "type": "",
                        "links": {
                            "self": [
                                {
                                    "href": ""
                                }
                            ]
                        }
                    },
                    "public": "",
                    "archived": "",
                    "links": {
                        "clone": [
                            {
                                "href": "",
                                "name": ""
                            }
                        ],
                        "self": [
                            {
                                "href": ""
                            }
                        ]
                    }
                }
            },
            "toRef": {
                "id": "",
                "displayId": "",
                "latestCommit": "",
                "type": "",
                "repository": {
                    "slug": "",
                    "id": "",
                    "name": "",
                    "hierarchyId": "",
                    "scmId": "",
                    "state": "",
                    "statusMessage": "",
                    "forkable": "",
                    "project": {
                        "key": "",
                        "id": "",
                        "name": "",
                        "public": "",
                        "type": "",
                        "links": {
                            "self": [
                                {
                                    "href": ""
                                }
                            ]
                        }
                    },
                    "public": "",
                    "archived": "",
                    "links": {
                        "clone": [
                            {
                                "href": "",
                                "name": ""
                            }
                        ],
                        "self": [
                            {
                                "href": ""
                            }
                        ]
                    }
                }
            },
            "locked": "",
            "author": {
                "user": {
                    "name": "",
                    "emailAddress": "",
                    "active": "",
                    "displayName": "",
                    "id": "",
                    "slug": "",
                    "type": "",
                    "links": {
                        "self": [
                            {
                                "href": ""
                            }
                        ]
                    }
                },
                "role": "",
                "approved": "",
                "status": ""
            },
            "reviewers": [],
            "participants": [],
            "properties": {
                "mergeResult": {
                    "outcome": "",
                    "current": ""
                },
                "resolvedTaskCount": "",
                "commentCount": "",
                "openTaskCount": ""
            },
            "links": {
                "self": [
                    {
                        "href": ""
                    }
                ]
            }
        }
    ],
    "start": ""
}</pre>

### operation: Merge Pull Request
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository in which to merge the pull request. You can select from the following options: Organization and User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, in which to merge the pull request.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, in which to merge the pull request.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository in which to merge the pull request.
</td></tr><tr><td>Pull Request ID</td><td>Specify The ID of the pull request to merge.
</td></tr><tr><td>Merge Commit Message</td><td>(Optional) Specify a message to attach to the merge commit.
</td></tr><tr><td>Strategy</td><td>(Optional) Specify the strategy used to merge pull request. You can choose from  'Merge Commit', 'Fast-forward', 'Fast-forward only', 'Rebase and merge', 'Rebase and fast-forward', 'Squash' or'Squash, fast-forward only'
</td></tr><tr><td>Version</td><td>(Optional) Specify the current version of the pull request. If the server's version isn't the same as the specified version the operation will fail. 
</td></tr><tr><td>Auto Subject</td><td>(Optional) Specify whether you want prepend auto-generated subject to the Merge Commit Message or not.
</td></tr><tr><td>Auto Merge</td><td>(Optional) Specify whether you want automatically merge this pull request when all check passes.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "open": "",
    "draft": "",
    "links": {
        "self": [
            {
                "href": ""
            }
        ]
    },
    "state": "",
    "title": "",
    "toRef": {
        "id": "",
        "type": "",
        "displayId": "",
        "repository": {
            "id": "",
            "name": "",
            "slug": "",
            "links": {
                "self": [
                    {
                        "href": ""
                    }
                ],
                "clone": [
                    {
                        "href": "",
                        "name": ""
                    }
                ]
            },
            "scmId": "",
            "state": "",
            "public": "",
            "project": {
                "id": "",
                "key": "",
                "name": "",
                "type": "",
                "links": {
                    "self": [
                        {
                            "href": ""
                        }
                    ]
                },
                "public": ""
            },
            "archived": "",
            "forkable": "",
            "hierarchyId": "",
            "statusMessage": ""
        },
        "latestCommit": ""
    },
    "author": {
        "role": "",
        "user": {
            "id": "",
            "name": "",
            "slug": "",
            "type": "",
            "links": {
                "self": [
                    {
                        "href": ""
                    }
                ]
            },
            "active": "",
            "displayName": "",
            "emailAddress": ""
        },
        "status": "",
        "approved": ""
    },
    "closed": "",
    "locked": "",
    "fromRef": {
        "id": "",
        "type": "",
        "displayId": "",
        "repository": {
            "id": "",
            "name": "",
            "slug": "",
            "links": {
                "self": [
                    {
                        "href": ""
                    }
                ],
                "clone": [
                    {
                        "href": "",
                        "name": ""
                    }
                ]
            },
            "scmId": "",
            "state": "",
            "public": "",
            "project": {
                "id": "",
                "key": "",
                "name": "",
                "type": "",
                "links": {
                    "self": [
                        {
                            "href": ""
                        }
                    ]
                },
                "public": ""
            },
            "archived": "",
            "forkable": "",
            "hierarchyId": "",
            "statusMessage": ""
        },
        "latestCommit": ""
    },
    "version": "",
    "reviewers": [],
    "closedDate": "",
    "properties": {
        "mergeCommit": {
            "id": "",
            "displayId": ""
        }
    },
    "createdDate": "",
    "updatedDate": "",
    "description": "",
    "participants": []
}</pre>

### operation: Create Pull Request
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository in which to create a pull request on Bitbucket. You can choose from Organization or User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, of the repository in which to create a pull request, in the Organization Name field.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, of the repository in which to create a pull request, in the Repository Owner field.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository on which you want to create a pull request on Bitbucket.
</td></tr><tr><td>Head Repository</td><td>Specify the name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace head with a user like this: username:branch.
</td></tr><tr><td>Base Branch</td><td>Specify the name of the branch to which you want to pull the changes. The branch to which you want to pull the changes should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository.
</td></tr><tr><td>Title</td><td>Specify the title of the new pull request that you want to create on Bitbucket.
</td></tr><tr><td>Description</td><td>Specify the contents of the new pull request that you want to create on Bitbucket.
</td></tr><tr><td>Reviewers</td><td>Specify the comma separated list of usernames to add as a reviewer to the pull request
</td></tr><tr><td>Draft</td><td>Select this option to create the pull request as a 'Draft'.
</td></tr><tr><td>Additional Fields</td><td>Specify the additional parameters in key-value format. For example,{
            "version": 2154,
            "open": true,
            "id": 1
          } For more information see, https://developer.atlassian.com/server/bitbucket/rest/v819/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-post
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "open": "",
    "draft": "",
    "links": {
        "self": [
            {
                "href": ""
            }
        ]
    },
    "state": "",
    "title": "",
    "description": "",
    "toRef": {
        "id": "",
        "type": "",
        "displayId": "",
        "repository": {
            "id": "",
            "name": "",
            "slug": "",
            "links": {
                "self": [
                    {
                        "href": ""
                    }
                ],
                "clone": [
                    {
                        "href": "",
                        "name": ""
                    }
                ]
            },
            "scmId": "",
            "state": "",
            "public": "",
            "project": {
                "id": "",
                "key": "",
                "name": "",
                "type": "",
                "links": {
                    "self": [
                        {
                            "href": ""
                        }
                    ]
                },
                "public": ""
            },
            "archived": "",
            "forkable": "",
            "hierarchyId": "",
            "statusMessage": ""
        },
        "latestCommit": ""
    },
    "author": {
        "role": "",
        "user": {
            "id": "",
            "name": "",
            "slug": "",
            "type": "",
            "links": {
                "self": [
                    {
                        "href": ""
                    }
                ]
            },
            "active": "",
            "displayName": "",
            "emailAddress": ""
        },
        "status": "",
        "approved": ""
    },
    "closed": "",
    "locked": "",
    "fromRef": {
        "id": "",
        "type": "",
        "displayId": "",
        "repository": {
            "id": "",
            "name": "",
            "slug": "",
            "links": {
                "self": [
                    {
                        "href": ""
                    }
                ],
                "clone": [
                    {
                        "href": "",
                        "name": ""
                    }
                ]
            },
            "scmId": "",
            "state": "",
            "public": "",
            "project": {
                "id": "",
                "key": "",
                "name": "",
                "type": "",
                "links": {
                    "self": [
                        {
                            "href": ""
                        }
                    ]
                },
                "public": ""
            },
            "archived": "",
            "forkable": "",
            "hierarchyId": "",
            "statusMessage": ""
        },
        "latestCommit": ""
    },
    "version": "",
    "reviewers": [],
    "createdDate": "",
    "updatedDate": "",
    "participants": []
}</pre>

### operation: Create Pull Request Comment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository in which to create a pull request comment. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, in which to create a pull request comment.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, in which to create a pull request comment.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository in which to create the pull request comment.
</td></tr><tr><td>Pull Request ID</td><td>Specify the ID of a pull request to create the comment.
</td></tr><tr><td>Description</td><td>Specify text for the pull request comment.
</td></tr><tr><td>Severity</td><td>Select the severity of the comment. You can choose from NORMAL: To add a comment, BLOCKER: To create a task.
</td></tr><tr><td>State</td><td>Select the state of the comment. You can choose from OPEN or PENDING.
</td></tr><tr><td>Other Fields</td><td>(Optional) Specify other fields in the JSON format
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "properties": {
        "repositoryId": ""
    },
    "id": "",
    "version": "",
    "text": "",
    "author": {
        "name": "",
        "emailAddress": "",
        "active": "",
        "displayName": "",
        "id": "",
        "slug": "",
        "type": "",
        "links": {
            "self": [
                {
                    "href": ""
                }
            ]
        }
    },
    "createdDate": "",
    "updatedDate": "",
    "comments": [],
    "threadResolved": "",
    "severity": "",
    "state": "",
    "permittedOperations": {
        "editable": "",
        "transitionable": "",
        "deletable": ""
    }
}</pre>

### operation: Get Tag List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository from which to retrieve the list of tags. You can select from the following options: Organization and User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, from which to retrieve the list of tag.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, from which to retrieve the list of tags.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository from which to retrieve the list of tags.
</td></tr><tr><td>Filter Text</td><td>Specify the filter text to retrieve the matching tags.
</td></tr><tr><td>Order By</td><td>(Optional) Select the sorting criteria to sort the results. You can select from the following options: ALPHABETICAL and MODIFICATION.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to return the results of the operation.
</td></tr><tr><td>Per Page</td><td>Specify the number of results, per page, that this operation should return.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "size": "",
    "limit": "",
    "start": "",
    "values": [
        {
            "id": "",
            "hash": "",
            "type": "",
            "displayId": "",
            "latestCommit": "",
            "latestChangeset": ""
        }
    ],
    "isLastPage": ""
}</pre>

### operation: Create Tag
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository in which to create the tag. You can select from the following options: Organization: and User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, in which to create the tag.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, in which to create the tag.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository in which to create the tag.
</td></tr><tr><td>Tag Name</td><td>Specify the tag from where the tag is created.
</td></tr><tr><td>Target Branch</td><td>(Optional) Specify the branch(ref) name or a commit ID from where the tag is to be created.
</td></tr><tr><td>Tag Message</td><td>(Optional) Specify the message to use if creating a new tag.
</td></tr><tr><td>Type</td><td>(Optional) Specify the type of tag which is to be created.
</td></tr><tr><td>Overwrite</td><td>Specify whether you want to overwrite tag if tag with same name already exists. By default , it is set to false.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "hash": "",
    "type": "",
    "displayId": "",
    "latestCommit": "",
    "latestChangeset": ""
}</pre>

### operation: Get Server URL
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "server_url": ""
}</pre>

### operation: Get Pull Request Comments
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository from which to retrieve the pull request comments. You can select from the following options: Organization, User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, from which to retrieve the pull request comments.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, from which to retrieve the pull request comments.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository from whose pull request the comments are to be retrieved.
</td></tr><tr><td>Pull Request ID</td><td>Specify the ID of a pull request whose comments are to be retrieved.
</td></tr><tr><td>From ID</td><td>(Optional) Select the sort order to sort the results. You can select from the following options: Ascending and Descending. Default sort order is Descending.
</td></tr><tr><td>From Type</td><td>(Optional) Select the type of the activity item specified by From ID. You can select from the following options: COMMENT, ACTIVITY. Note: Required if From ID parameter is provided.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to return the results of the operation.
</td></tr><tr><td>Per Page</td><td>(Optional) Specify the number of results, per page, that this operation should return.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "size": "",
    "limit": "",
    "isLastPage": "",
    "values": [
        {
            "id": "",
            "createdDate": "",
            "user": {
                "name": "",
                "emailAddress": "",
                "active": "",
                "displayName": "",
                "id": "",
                "slug": "",
                "type": "",
                "links": {
                    "self": [
                        {
                            "href": ""
                        }
                    ]
                }
            },
            "action": "",
            "commentAction": "",
            "comment": {
                "properties": {
                    "repositoryId": ""
                },
                "id": "",
                "version": "",
                "text": "",
                "author": {
                    "name": "",
                    "emailAddress": "",
                    "active": "",
                    "displayName": "",
                    "id": "",
                    "slug": "",
                    "type": "",
                    "links": {
                        "self": [
                            {
                                "href": ""
                            }
                        ]
                    }
                },
                "createdDate": "",
                "updatedDate": "",
                "comments": [],
                "threadResolved": "",
                "severity": "",
                "state": "",
                "permittedOperations": {
                    "editable": "",
                    "transitionable": "",
                    "deletable": ""
                }
            }
        }
    ],
    "start": ""
}</pre>

### operation: Clone Repository
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Repository Type</td><td>Select the type of the repository to clone. You can select from the following options: Organization and User.
<br><strong>If you choose 'Organization'</strong><ul><li>Organization Name: Specify the name of the organization on Bitbucket, to clone.</li></ul><strong>If you choose 'User'</strong><ul><li>Repository Owner: Specify the name of the repository owner on Bitbucket, to clone.</li></ul></td></tr><tr><td>Repository Name</td><td>Specify the name of the repository to clone.
</td></tr><tr><td>Branch Name</td><td>Specify the branch name of the repository to clone.
</td></tr><tr><td>Clone As ZIP</td><td>Select this option to clone the specified repository as a zip file.
<br><strong>If you choose 'true'</strong><ul><li>Archive Format: Select an archive format from the following options. You can choose from zip, tar.gz, tar, tar.bz2.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "path": ""
}</pre>

### operation: Update Remote Repository
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>FortiSOAR File IRI</td><td>Specify the FortiSOAR file IRI whose changes replace in the specified local repository.
</td></tr><tr><td>Cloned Repository Path</td><td>Specify the path of the cloned repository to which to apply the changes of the specified FortiSOAR file.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": ""
}</pre>

## Included playbooks
The `Sample - bitbucket - 1.0.0` playbook collection comes bundled with the Bitbucket connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Bitbucket connector.

- Clone Repository
- Create Pull Request
- Create Pull Request Comment
- Create Repository
- Create Repository Branch
- Create Tag
- Create or Update File Contents
- Delete Repository
- Delete Repository Branch
- Get File Details
- Get Member List of Repository
- Get Pull Request Comments
- Get Pull Request List
- Get Repository Branch List
- Get Server URL
- Get Tag List
- Merge Pull Request
- Update Remote Repository
- Update User Repository Permission

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
