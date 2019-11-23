"""
env PYTHONIOENCODING=UTF-8 PYTHONUNBUFFERED=1
"""
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import datetime

# 1. Import the library
import appcenter

access_token = "a97d856191e9ade9b2942c900f67ceb9349e5980"
owner = "benkcchan"
myapp = "App-Test"
binary_path = "/Users/jayleeli/work/python/project/Python-study/demo_py3/temp/app-malaysia-production-general-release.apk"
group_id = "65bc8cd6-347c-46ae-96bf-53b9095c7495"

# 2. Create a new client
client = appcenter.AppCenterClient(access_token=access_token)

# 3. Check some error groups
start = datetime.datetime.now() - datetime.timedelta(days=10)
for group in client.crashes.get_error_groups(owner_name=owner, app_name=myapp, start_time=start):
    print(group.errorGroupId)
    
# 4. Get recent versions
for version in client.versions.all(owner_name=owner, app_name=myapp):
    print(version)
    
# 5. Create a new release
result = client.versions.upload_and_release(
    owner_name=owner,
    app_name=myapp,
    version="0.1",
    build_number="123",
    binary_path=binary_path,
    group_id=group_id,
    release_notes="These are some release notes",
    branch_name="test_branch",
    commit_hash="1234567890123456789012345678901234567890",
    commit_message="This is a commit message"
)

print(result)