"""Transactional write/commit for config files"""
from . import twrite, nbio
import os, logging, tempfile, shutil

log = logging.getLogger(__name__)


def commonpath(paths):
    if hasattr(os.path, 'commonpath'):
        return os.path.commonpath(paths)
    else:
        abs_paths = [os.path.normpath(os.path.abspath(p)).split('/') for p in paths]
        result = []
        for segments in zip(*abs_paths):
            element = segments[0]
            for seg in segments[1:]:
                if seg != element:
                    return '/'.join(result) if result else '/'
            result.append(element)
        return '/'.join(result)


class FSTransaction(object):
    def __init__(self, target_dir, work_dir=None):
        self.target_dir = target_dir.rstrip('/')
        self.temp_path = work_dir or os.path.join(self.target_dir, '.transaction')
        self.writer = os.path.join(self.temp_path, 'write')
        self.recover = os.path.join(self.temp_path, 'recover')
        if not os.path.exists(self.writer):
            os.makedirs(self.writer)
        if not os.path.exists(self.recover):
            os.makedirs(self.recover)
        self.to_delete = []
        self.recover_delete = []
        self.in_transaction = []
        self.in_recovery = []

    def copy(self, source, path):
        """Copy the given source to the target path"""
        relative = self.relative_path(path)
        if os.path.exists(source):
            return self._copy_source_to_root(source, self.writer, relative)
        return None

    def _copy_source_to_root(self, source, root, relative):
        """Copy source-file into root/relative"""
        recovery = os.path.join(root, relative)
        dirname = os.path.dirname(recovery)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        if os.path.islink(source):
            link_dest = os.readlink(source)
            if os.path.exists(recovery):
                os.remove(recovery)
            os.symlink(link_dest, recovery)
        else:
            shutil.copy2(source, os.path.join(root, relative))
        return recovery

    def twrite(self, path, content):
        """Transactional twrite operation"""
        relative = self.save_path(path)
        if not os.path.exists(path):
            self.recover_delete.append(path)
        written = os.path.join(self.writer, relative.lstrip('/'))
        twrite.twrite(written, content)
        return written

    def chmod(self, path, mode=0o644):
        """Set mode of the path to given mode within transaction"""
        relative = self.save_path(path)
        written = os.path.join(self.writer, relative)
        if not os.path.exists(written):
            shutil.copy2(path, written)
        os.chmod(written, mode)

    def chown(self, path, *args, **named):
        """Change ownership of a file within transaction"""
        relative = self.save_path(path)
        written = os.path.join(self.writer, relative)
        if not os.path.exists(written):
            shutil.copy2(path, written)
        os.chown(written, *args, **named)

    def relative_path(self, path):
        if not path.startswith('/'):
            path = os.path.join(self.target_dir, path)
        prefix = commonpath([self.target_dir, path])
        if prefix != self.target_dir:
            raise ValueError("Need a sub-path of %r: %r", self.target_dir, path)
        relative = path[len(prefix) :].lstrip('/')
        return relative

    def writer_path(self, path):
        """Calculate the path for writing to given path"""
        return os.path.join(self.writer, self.relative_path(path))

    def recovery_path(self, path):
        """Calculate the path for saving files for restore"""
        return os.path.join(self.writer, self.relative_path(path))

    def debug_description(self):
        """Create a debugging description of our operations"""
        description = nbio.Process(
            [
                'tree',
                self.temp_path,
            ]
        )().decode('utf-8', 'ignore')
        return description

    def save_path(self, path):
        """Utility to save the content, state, ownership etc of file"""
        relative = self.relative_path(path)
        if os.path.exists(path):
            self._copy_source_to_root(path, self.recover, relative)
        return relative

    def remove(self, path):
        """Delete a path during the transaction"""
        relative = self.save_path(path)
        self.to_delete.append(os.path.join(self.target_dir, relative))

    def symlink(self, target, link):
        """Create link pointing to target"""
        relative = self.save_path(link)
        final = os.path.join(self.writer, relative)
        os.symlink(target, final)
        return final

    def add_to_transaction(self, command, *args, **named):
        """Add a callable that must run inside the transaction (failure cancels)"""
        self.in_transaction.append((command, args, named))

    def add_to_recovery(self, command, *args, **named):
        """Add a callable that should run after recovery"""
        self.in_recovery.append((command, args, named))

    def would_write(self, path):
        """Would we write to the given path?"""
        relative = self.relative_path(path)
        return os.path.exists(os.path.join(self.writer, relative))

    def would_remove(self, path):
        """Would we delete the given path?"""
        relative = self.relative_path(path)
        return os.path.join(self.target_dir, relative) in self.to_delete

    def _rsync_source_to_dest(self, source, dest):
        """Run rsync from source to destination"""
        command = (
            ['rsync', '-av']
            + [os.path.join(source, x) for x in os.listdir(source)]
            + [
                dest + '/',
            ]
        )
        log.info(" %s", " ".join(command))
        try:
            nbio.Process(command)()
        except nbio.ProcessError as err:
            log.warning("rsync operation failed")
            raise RuntimeError('Failure during %s' % (" ".join(command)))
        else:
            return True

    def commit(self):
        """Attempt to commit changes to the transaction"""
        try:
            self._rsync_source_to_dest(self.writer, self.target_dir)
            for filename in self.to_delete:
                log.debug("  rm: %s", filename)
                if os.path.exists(filename):
                    os.remove(filename)
            for callable, args, named in self.in_transaction:
                log.debug("  run: %s", callable)
                callable(*args, **named)
        except Exception as err:
            log.exception("Unable to commit changes")
            try:
                self.abort()
            except Exception as abort_err:
                log.exception("Failure during abort, filesystem state inconsistent")
                raise abort_err
            return False
        else:
            self.cleanup()
            return True

    def abort(self):
        """Abort commit, attempt to restore previous"""
        log.debug("Aborting from: %s", self.target_dir)
        self._rsync_source_to_dest(self.recover, self.target_dir)
        for filename in self.recover_delete:
            if os.path.exists(filename):
                os.remove(filename)
        for callable, args, named in self.in_recovery:
            callable(*args, **named)

    def cleanup(self):
        shutil.rmtree(self.temp_path)