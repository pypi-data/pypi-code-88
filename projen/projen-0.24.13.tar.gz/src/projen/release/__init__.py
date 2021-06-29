import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import (
    Component as _Component_2b0ad27f,
    Project as _Project_57d89203,
    Publisher as _Publisher_8d82749b,
)
from ..github.workflows import Job as _Job_20ffcf45, JobStep as _JobStep_c3287c05
from ..tasks import Task as _Task_fb843092


@jsii.data_type(
    jsii_type="projen.release.BranchOptions",
    jsii_struct_bases=[],
    name_mapping={
        "major_version": "majorVersion",
        "prerelease": "prerelease",
        "workflow_name": "workflowName",
    },
)
class BranchOptions:
    def __init__(
        self,
        *,
        major_version: jsii.Number,
        prerelease: typing.Optional[builtins.str] = None,
        workflow_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for a release branch.

        :param major_version: (experimental) The major versions released from this branch.
        :param prerelease: (experimental) Bump the version as a pre-release tag. Default: - normal releases
        :param workflow_name: (experimental) The name of the release workflow. Default: "release-BRANCH"

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "major_version": major_version,
        }
        if prerelease is not None:
            self._values["prerelease"] = prerelease
        if workflow_name is not None:
            self._values["workflow_name"] = workflow_name

    @builtins.property
    def major_version(self) -> jsii.Number:
        '''(experimental) The major versions released from this branch.

        :stability: experimental
        '''
        result = self._values.get("major_version")
        assert result is not None, "Required property 'major_version' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def prerelease(self) -> typing.Optional[builtins.str]:
        '''(experimental) Bump the version as a pre-release tag.

        :default: - normal releases

        :stability: experimental
        '''
        result = self._values.get("prerelease")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workflow_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the release workflow.

        :default: "release-BRANCH"

        :stability: experimental
        '''
        result = self._values.get("workflow_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Release(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.release.Release",
):
    '''(experimental) Manages releases (currently through GitHub workflows).

    By default, no branches are released. To add branches, call ``addBranch()``.

    :stability: experimental
    '''

    def __init__(
        self,
        project: _Project_57d89203,
        *,
        branch: builtins.str,
        task: _Task_fb843092,
        version_file: builtins.str,
        antitamper: typing.Optional[builtins.bool] = None,
        artifacts_directory: typing.Optional[builtins.str] = None,
        jsii_release_version: typing.Optional[builtins.str] = None,
        major_version: typing.Optional[jsii.Number] = None,
        post_build_steps: typing.Optional[typing.Sequence[_JobStep_c3287c05]] = None,
        prerelease: typing.Optional[builtins.str] = None,
        release_branches: typing.Optional[typing.Mapping[builtins.str, BranchOptions]] = None,
        release_every_commit: typing.Optional[builtins.bool] = None,
        release_schedule: typing.Optional[builtins.str] = None,
        release_workflow_name: typing.Optional[builtins.str] = None,
        release_workflow_setup_steps: typing.Optional[typing.Sequence[_JobStep_c3287c05]] = None,
        workflow_container_image: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project: -
        :param branch: (experimental) The default branch name to release from. Use ``majorVersion`` to restrict this branch to only publish releases with a specific major version. You can add additional branches using ``addBranch()``.
        :param task: (experimental) The task to execute in order to create the release artifacts. Artifacts are expected to reside under ``artifactsDirectory`` (defaults to ``dist/``) once build is complete.
        :param version_file: (experimental) A name of a .json file to set the ``version`` field in after a bump.
        :param antitamper: (experimental) Checks that after build there are no modified files on git. Default: true
        :param artifacts_directory: (experimental) A directory which will contain artifacts to be published to npm. Default: "dist"
        :param jsii_release_version: (experimental) Version requirement of ``jsii-release`` which is used to publish modules to npm. Default: "latest"
        :param major_version: (experimental) Major version to release from the default branch. If this is specified, we bump the latest version of this major version line. If not specified, we bump the global latest version. Default: - Major version is not enforced.
        :param post_build_steps: (experimental) Steps to execute after build as part of the release workflow. Default: []
        :param prerelease: (experimental) Bump versions from the default branch as pre-releases (e.g. "beta", "alpha", "pre"). Default: - normal semantic versions
        :param release_branches: (experimental) Defines additional release branches. A workflow will be created for each release branch which will publish releases from commits in this branch. Each release branch *must* be assigned a major version number which is used to enforce that versions published from that branch always use that major version. If multiple branches are used, the ``majorVersion`` field must also be provided for the default branch. Default: - no additional branches are used for release. you can use ``addBranch()`` to add additional branches.
        :param release_every_commit: (experimental) Automatically release new versions every commit to one of branches in ``releaseBranches``. Default: true
        :param release_schedule: (experimental) CRON schedule to trigger new releases. Default: - no scheduled releases
        :param release_workflow_name: (experimental) The name of the default release workflow. Default: "Release"
        :param release_workflow_setup_steps: (experimental) A set of workflow steps to execute in order to setup the workflow container.
        :param workflow_container_image: (experimental) Container image to use for GitHub workflows. Default: - default image

        :stability: experimental
        '''
        options = ReleaseOptions(
            branch=branch,
            task=task,
            version_file=version_file,
            antitamper=antitamper,
            artifacts_directory=artifacts_directory,
            jsii_release_version=jsii_release_version,
            major_version=major_version,
            post_build_steps=post_build_steps,
            prerelease=prerelease,
            release_branches=release_branches,
            release_every_commit=release_every_commit,
            release_schedule=release_schedule,
            release_workflow_name=release_workflow_name,
            release_workflow_setup_steps=release_workflow_setup_steps,
            workflow_container_image=workflow_container_image,
        )

        jsii.create(Release, self, [project, options])

    @jsii.member(jsii_name="addBranch")
    def add_branch(
        self,
        branch: builtins.str,
        *,
        major_version: jsii.Number,
        prerelease: typing.Optional[builtins.str] = None,
        workflow_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Adds a release branch.

        It is a git branch from which releases are published. If a project has more than one release
        branch, we require that ``majorVersion`` is also specified for the primary branch in order to
        ensure branches always release the correct version.

        :param branch: The branch to monitor (e.g. ``main``, ``v2.x``).
        :param major_version: (experimental) The major versions released from this branch.
        :param prerelease: (experimental) Bump the version as a pre-release tag. Default: - normal releases
        :param workflow_name: (experimental) The name of the release workflow. Default: "release-BRANCH"

        :stability: experimental
        '''
        options = BranchOptions(
            major_version=major_version,
            prerelease=prerelease,
            workflow_name=workflow_name,
        )

        return typing.cast(None, jsii.invoke(self, "addBranch", [branch, options]))

    @jsii.member(jsii_name="addJobs")
    def add_jobs(self, jobs: typing.Mapping[builtins.str, _Job_20ffcf45]) -> None:
        '''(experimental) Adds jobs to all release workflows.

        :param jobs: The jobs to add (name => job).

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addJobs", [jobs]))

    @jsii.member(jsii_name="preSynthesize")
    def pre_synthesize(self) -> None:
        '''(experimental) Called before synthesis.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "preSynthesize", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> _Publisher_8d82749b:
        '''(experimental) Package publisher.

        :stability: experimental
        '''
        return typing.cast(_Publisher_8d82749b, jsii.get(self, "publisher"))


@jsii.data_type(
    jsii_type="projen.release.ReleaseProjectOptions",
    jsii_struct_bases=[],
    name_mapping={
        "antitamper": "antitamper",
        "artifacts_directory": "artifactsDirectory",
        "jsii_release_version": "jsiiReleaseVersion",
        "major_version": "majorVersion",
        "post_build_steps": "postBuildSteps",
        "prerelease": "prerelease",
        "release_branches": "releaseBranches",
        "release_every_commit": "releaseEveryCommit",
        "release_schedule": "releaseSchedule",
        "release_workflow_name": "releaseWorkflowName",
        "release_workflow_setup_steps": "releaseWorkflowSetupSteps",
        "workflow_container_image": "workflowContainerImage",
    },
)
class ReleaseProjectOptions:
    def __init__(
        self,
        *,
        antitamper: typing.Optional[builtins.bool] = None,
        artifacts_directory: typing.Optional[builtins.str] = None,
        jsii_release_version: typing.Optional[builtins.str] = None,
        major_version: typing.Optional[jsii.Number] = None,
        post_build_steps: typing.Optional[typing.Sequence[_JobStep_c3287c05]] = None,
        prerelease: typing.Optional[builtins.str] = None,
        release_branches: typing.Optional[typing.Mapping[builtins.str, BranchOptions]] = None,
        release_every_commit: typing.Optional[builtins.bool] = None,
        release_schedule: typing.Optional[builtins.str] = None,
        release_workflow_name: typing.Optional[builtins.str] = None,
        release_workflow_setup_steps: typing.Optional[typing.Sequence[_JobStep_c3287c05]] = None,
        workflow_container_image: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Project options for release.

        :param antitamper: (experimental) Checks that after build there are no modified files on git. Default: true
        :param artifacts_directory: (experimental) A directory which will contain artifacts to be published to npm. Default: "dist"
        :param jsii_release_version: (experimental) Version requirement of ``jsii-release`` which is used to publish modules to npm. Default: "latest"
        :param major_version: (experimental) Major version to release from the default branch. If this is specified, we bump the latest version of this major version line. If not specified, we bump the global latest version. Default: - Major version is not enforced.
        :param post_build_steps: (experimental) Steps to execute after build as part of the release workflow. Default: []
        :param prerelease: (experimental) Bump versions from the default branch as pre-releases (e.g. "beta", "alpha", "pre"). Default: - normal semantic versions
        :param release_branches: (experimental) Defines additional release branches. A workflow will be created for each release branch which will publish releases from commits in this branch. Each release branch *must* be assigned a major version number which is used to enforce that versions published from that branch always use that major version. If multiple branches are used, the ``majorVersion`` field must also be provided for the default branch. Default: - no additional branches are used for release. you can use ``addBranch()`` to add additional branches.
        :param release_every_commit: (experimental) Automatically release new versions every commit to one of branches in ``releaseBranches``. Default: true
        :param release_schedule: (experimental) CRON schedule to trigger new releases. Default: - no scheduled releases
        :param release_workflow_name: (experimental) The name of the default release workflow. Default: "Release"
        :param release_workflow_setup_steps: (experimental) A set of workflow steps to execute in order to setup the workflow container.
        :param workflow_container_image: (experimental) Container image to use for GitHub workflows. Default: - default image

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if antitamper is not None:
            self._values["antitamper"] = antitamper
        if artifacts_directory is not None:
            self._values["artifacts_directory"] = artifacts_directory
        if jsii_release_version is not None:
            self._values["jsii_release_version"] = jsii_release_version
        if major_version is not None:
            self._values["major_version"] = major_version
        if post_build_steps is not None:
            self._values["post_build_steps"] = post_build_steps
        if prerelease is not None:
            self._values["prerelease"] = prerelease
        if release_branches is not None:
            self._values["release_branches"] = release_branches
        if release_every_commit is not None:
            self._values["release_every_commit"] = release_every_commit
        if release_schedule is not None:
            self._values["release_schedule"] = release_schedule
        if release_workflow_name is not None:
            self._values["release_workflow_name"] = release_workflow_name
        if release_workflow_setup_steps is not None:
            self._values["release_workflow_setup_steps"] = release_workflow_setup_steps
        if workflow_container_image is not None:
            self._values["workflow_container_image"] = workflow_container_image

    @builtins.property
    def antitamper(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Checks that after build there are no modified files on git.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("antitamper")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def artifacts_directory(self) -> typing.Optional[builtins.str]:
        '''(experimental) A directory which will contain artifacts to be published to npm.

        :default: "dist"

        :stability: experimental
        '''
        result = self._values.get("artifacts_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jsii_release_version(self) -> typing.Optional[builtins.str]:
        '''(experimental) Version requirement of ``jsii-release`` which is used to publish modules to npm.

        :default: "latest"

        :stability: experimental
        '''
        result = self._values.get("jsii_release_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def major_version(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Major version to release from the default branch.

        If this is specified, we bump the latest version of this major version line.
        If not specified, we bump the global latest version.

        :default: - Major version is not enforced.

        :stability: experimental
        '''
        result = self._values.get("major_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def post_build_steps(self) -> typing.Optional[typing.List[_JobStep_c3287c05]]:
        '''(experimental) Steps to execute after build as part of the release workflow.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("post_build_steps")
        return typing.cast(typing.Optional[typing.List[_JobStep_c3287c05]], result)

    @builtins.property
    def prerelease(self) -> typing.Optional[builtins.str]:
        '''(experimental) Bump versions from the default branch as pre-releases (e.g. "beta", "alpha", "pre").

        :default: - normal semantic versions

        :stability: experimental
        '''
        result = self._values.get("prerelease")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_branches(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, BranchOptions]]:
        '''(experimental) Defines additional release branches.

        A workflow will be created for each
        release branch which will publish releases from commits in this branch.
        Each release branch *must* be assigned a major version number which is used
        to enforce that versions published from that branch always use that major
        version. If multiple branches are used, the ``majorVersion`` field must also
        be provided for the default branch.

        :default:

        - no additional branches are used for release. you can use
        ``addBranch()`` to add additional branches.

        :stability: experimental
        '''
        result = self._values.get("release_branches")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, BranchOptions]], result)

    @builtins.property
    def release_every_commit(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Automatically release new versions every commit to one of branches in ``releaseBranches``.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("release_every_commit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def release_schedule(self) -> typing.Optional[builtins.str]:
        '''(experimental) CRON schedule to trigger new releases.

        :default: - no scheduled releases

        :stability: experimental
        '''
        result = self._values.get("release_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_workflow_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the default release workflow.

        :default: "Release"

        :stability: experimental
        '''
        result = self._values.get("release_workflow_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_workflow_setup_steps(
        self,
    ) -> typing.Optional[typing.List[_JobStep_c3287c05]]:
        '''(experimental) A set of workflow steps to execute in order to setup the workflow container.

        :stability: experimental
        '''
        result = self._values.get("release_workflow_setup_steps")
        return typing.cast(typing.Optional[typing.List[_JobStep_c3287c05]], result)

    @builtins.property
    def workflow_container_image(self) -> typing.Optional[builtins.str]:
        '''(experimental) Container image to use for GitHub workflows.

        :default: - default image

        :stability: experimental
        '''
        result = self._values.get("workflow_container_image")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReleaseProjectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.release.ReleaseOptions",
    jsii_struct_bases=[ReleaseProjectOptions],
    name_mapping={
        "antitamper": "antitamper",
        "artifacts_directory": "artifactsDirectory",
        "jsii_release_version": "jsiiReleaseVersion",
        "major_version": "majorVersion",
        "post_build_steps": "postBuildSteps",
        "prerelease": "prerelease",
        "release_branches": "releaseBranches",
        "release_every_commit": "releaseEveryCommit",
        "release_schedule": "releaseSchedule",
        "release_workflow_name": "releaseWorkflowName",
        "release_workflow_setup_steps": "releaseWorkflowSetupSteps",
        "workflow_container_image": "workflowContainerImage",
        "branch": "branch",
        "task": "task",
        "version_file": "versionFile",
    },
)
class ReleaseOptions(ReleaseProjectOptions):
    def __init__(
        self,
        *,
        antitamper: typing.Optional[builtins.bool] = None,
        artifacts_directory: typing.Optional[builtins.str] = None,
        jsii_release_version: typing.Optional[builtins.str] = None,
        major_version: typing.Optional[jsii.Number] = None,
        post_build_steps: typing.Optional[typing.Sequence[_JobStep_c3287c05]] = None,
        prerelease: typing.Optional[builtins.str] = None,
        release_branches: typing.Optional[typing.Mapping[builtins.str, BranchOptions]] = None,
        release_every_commit: typing.Optional[builtins.bool] = None,
        release_schedule: typing.Optional[builtins.str] = None,
        release_workflow_name: typing.Optional[builtins.str] = None,
        release_workflow_setup_steps: typing.Optional[typing.Sequence[_JobStep_c3287c05]] = None,
        workflow_container_image: typing.Optional[builtins.str] = None,
        branch: builtins.str,
        task: _Task_fb843092,
        version_file: builtins.str,
    ) -> None:
        '''(experimental) Options for ``Release``.

        :param antitamper: (experimental) Checks that after build there are no modified files on git. Default: true
        :param artifacts_directory: (experimental) A directory which will contain artifacts to be published to npm. Default: "dist"
        :param jsii_release_version: (experimental) Version requirement of ``jsii-release`` which is used to publish modules to npm. Default: "latest"
        :param major_version: (experimental) Major version to release from the default branch. If this is specified, we bump the latest version of this major version line. If not specified, we bump the global latest version. Default: - Major version is not enforced.
        :param post_build_steps: (experimental) Steps to execute after build as part of the release workflow. Default: []
        :param prerelease: (experimental) Bump versions from the default branch as pre-releases (e.g. "beta", "alpha", "pre"). Default: - normal semantic versions
        :param release_branches: (experimental) Defines additional release branches. A workflow will be created for each release branch which will publish releases from commits in this branch. Each release branch *must* be assigned a major version number which is used to enforce that versions published from that branch always use that major version. If multiple branches are used, the ``majorVersion`` field must also be provided for the default branch. Default: - no additional branches are used for release. you can use ``addBranch()`` to add additional branches.
        :param release_every_commit: (experimental) Automatically release new versions every commit to one of branches in ``releaseBranches``. Default: true
        :param release_schedule: (experimental) CRON schedule to trigger new releases. Default: - no scheduled releases
        :param release_workflow_name: (experimental) The name of the default release workflow. Default: "Release"
        :param release_workflow_setup_steps: (experimental) A set of workflow steps to execute in order to setup the workflow container.
        :param workflow_container_image: (experimental) Container image to use for GitHub workflows. Default: - default image
        :param branch: (experimental) The default branch name to release from. Use ``majorVersion`` to restrict this branch to only publish releases with a specific major version. You can add additional branches using ``addBranch()``.
        :param task: (experimental) The task to execute in order to create the release artifacts. Artifacts are expected to reside under ``artifactsDirectory`` (defaults to ``dist/``) once build is complete.
        :param version_file: (experimental) A name of a .json file to set the ``version`` field in after a bump.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "branch": branch,
            "task": task,
            "version_file": version_file,
        }
        if antitamper is not None:
            self._values["antitamper"] = antitamper
        if artifacts_directory is not None:
            self._values["artifacts_directory"] = artifacts_directory
        if jsii_release_version is not None:
            self._values["jsii_release_version"] = jsii_release_version
        if major_version is not None:
            self._values["major_version"] = major_version
        if post_build_steps is not None:
            self._values["post_build_steps"] = post_build_steps
        if prerelease is not None:
            self._values["prerelease"] = prerelease
        if release_branches is not None:
            self._values["release_branches"] = release_branches
        if release_every_commit is not None:
            self._values["release_every_commit"] = release_every_commit
        if release_schedule is not None:
            self._values["release_schedule"] = release_schedule
        if release_workflow_name is not None:
            self._values["release_workflow_name"] = release_workflow_name
        if release_workflow_setup_steps is not None:
            self._values["release_workflow_setup_steps"] = release_workflow_setup_steps
        if workflow_container_image is not None:
            self._values["workflow_container_image"] = workflow_container_image

    @builtins.property
    def antitamper(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Checks that after build there are no modified files on git.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("antitamper")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def artifacts_directory(self) -> typing.Optional[builtins.str]:
        '''(experimental) A directory which will contain artifacts to be published to npm.

        :default: "dist"

        :stability: experimental
        '''
        result = self._values.get("artifacts_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jsii_release_version(self) -> typing.Optional[builtins.str]:
        '''(experimental) Version requirement of ``jsii-release`` which is used to publish modules to npm.

        :default: "latest"

        :stability: experimental
        '''
        result = self._values.get("jsii_release_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def major_version(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Major version to release from the default branch.

        If this is specified, we bump the latest version of this major version line.
        If not specified, we bump the global latest version.

        :default: - Major version is not enforced.

        :stability: experimental
        '''
        result = self._values.get("major_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def post_build_steps(self) -> typing.Optional[typing.List[_JobStep_c3287c05]]:
        '''(experimental) Steps to execute after build as part of the release workflow.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("post_build_steps")
        return typing.cast(typing.Optional[typing.List[_JobStep_c3287c05]], result)

    @builtins.property
    def prerelease(self) -> typing.Optional[builtins.str]:
        '''(experimental) Bump versions from the default branch as pre-releases (e.g. "beta", "alpha", "pre").

        :default: - normal semantic versions

        :stability: experimental
        '''
        result = self._values.get("prerelease")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_branches(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, BranchOptions]]:
        '''(experimental) Defines additional release branches.

        A workflow will be created for each
        release branch which will publish releases from commits in this branch.
        Each release branch *must* be assigned a major version number which is used
        to enforce that versions published from that branch always use that major
        version. If multiple branches are used, the ``majorVersion`` field must also
        be provided for the default branch.

        :default:

        - no additional branches are used for release. you can use
        ``addBranch()`` to add additional branches.

        :stability: experimental
        '''
        result = self._values.get("release_branches")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, BranchOptions]], result)

    @builtins.property
    def release_every_commit(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Automatically release new versions every commit to one of branches in ``releaseBranches``.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("release_every_commit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def release_schedule(self) -> typing.Optional[builtins.str]:
        '''(experimental) CRON schedule to trigger new releases.

        :default: - no scheduled releases

        :stability: experimental
        '''
        result = self._values.get("release_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_workflow_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the default release workflow.

        :default: "Release"

        :stability: experimental
        '''
        result = self._values.get("release_workflow_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_workflow_setup_steps(
        self,
    ) -> typing.Optional[typing.List[_JobStep_c3287c05]]:
        '''(experimental) A set of workflow steps to execute in order to setup the workflow container.

        :stability: experimental
        '''
        result = self._values.get("release_workflow_setup_steps")
        return typing.cast(typing.Optional[typing.List[_JobStep_c3287c05]], result)

    @builtins.property
    def workflow_container_image(self) -> typing.Optional[builtins.str]:
        '''(experimental) Container image to use for GitHub workflows.

        :default: - default image

        :stability: experimental
        '''
        result = self._values.get("workflow_container_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def branch(self) -> builtins.str:
        '''(experimental) The default branch name to release from.

        Use ``majorVersion`` to restrict this branch to only publish releases with a
        specific major version.

        You can add additional branches using ``addBranch()``.

        :stability: experimental
        '''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task(self) -> _Task_fb843092:
        '''(experimental) The task to execute in order to create the release artifacts.

        Artifacts are
        expected to reside under ``artifactsDirectory`` (defaults to ``dist/``) once
        build is complete.

        :stability: experimental
        '''
        result = self._values.get("task")
        assert result is not None, "Required property 'task' is missing"
        return typing.cast(_Task_fb843092, result)

    @builtins.property
    def version_file(self) -> builtins.str:
        '''(experimental) A name of a .json file to set the ``version`` field in after a bump.

        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            "package.json"
        '''
        result = self._values.get("version_file")
        assert result is not None, "Required property 'version_file' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReleaseOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BranchOptions",
    "Release",
    "ReleaseOptions",
    "ReleaseProjectOptions",
]

publication.publish()
