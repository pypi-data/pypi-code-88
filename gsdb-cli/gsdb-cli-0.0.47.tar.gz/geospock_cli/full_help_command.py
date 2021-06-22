# Copyright (c) 2014-2021 GeoSpock Ltd.

import click


class FullHelpCommand(click.Command):
    def get_short_help_str(self, limit=None):
        """Displays full help text if short help text is absent."""
        return self.short_help or self.help or ""


class FullHelpGroup(click.Group):
    def get_short_help_str(self, limit=None):
        """Displays full help text if short help text is absent."""
        return self.short_help or self.help or ""
