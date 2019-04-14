#!/bin/python3
from cpt.packager import ConanMultiPackager
from conans import tools
import subprocess, os, sys

def build(channel, commit, password, version):
    builder = ConanMultiPackager(username="bentoudev", 
                upload="https://api.bintray.com/conan/bentoudev/yage", 
                channel=channel,
                stable_branch_pattern='release*', # channel is set explicitly!
                password=password)

    builder.add(settings={"arch": "x86_64", "build_type": "Release"},
                options={},
                env_vars={'AGNES_COMMIT':commit, 'AGNES_VERSION':version},
                build_requires={})

    builder.run()

def runCommand(args):
    if len(args) == 0:
        return None
    try:
        cmd = subprocess.run(args, encoding='utf-8', stdout=subprocess.PIPE)
        cmd.check_returncode()
        return cmd.stdout.split('\n')[0]
    except Exception as error:
        return None

def getGitVersion():
    try:
        data = {}
        data['version'] = runCommand(['git', 'describe'])
        data['commit'] = runCommand(['git', 'rev-parse', 'HEAD'])
        return data
    except Exception as error:
        return None

def execute(password):
    channel = 'dev'
    version = None
    gitData = getGitVersion()

    print ('')
    if 'CI' in os.environ:
        print(' [info] CI Environment detected')

        if 'APPVEYOR' in os.environ:
            print("APP_VEYOR: " + os.environ['APPVEYOR'])
            if 'APPVEYOR_REPO_TAG_NAME' in os.environ:
                version = os.environ['APPVEYOR_REPO_TAG_NAME']
                channel = 'stable'

        if 'TRAVIS' in os.environ:
            print("TRAVIS: " + os.environ['TRAVIS'])
            os.environ['CXX'] = 'clang++-5.0'
            os.environ['CC'] = 'clang-5.0'
            if 'TRAVIS_TAG' in os.environ:
                version = os.environ['TRAVIS_TAG']
                channel = 'stable'

    if not version:
        version = gitData['version']

    commit = gitData['commit']

    print (' [info] Channel: ' + channel)
    print (' [info] Version: ' + version)
    print (' [info] Commit: ' + commit)
    print ('')
    print (' [*] Executing conan build...')

    build(channel, commit, password, version)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        execute(sys.argv[1])
    else:
        print("Missing repository key argument!", file=sys.stderr)