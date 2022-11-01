"""Import all days and run to compare times"""

import os
import importlib
from tools.day_module import RunDay

class RunYears:
    """
    Import all Advent of Code days and compare runnning times.
    """

    def __init__(self) -> None:
        """
        Import all the day's of Advent of code as plugins.
        """
        days_paths = os.listdir('solutions/year_2021/days')
        days_paths.sort()

        self.days = []

        for path in days_paths:
            if self._is_plugin_path(path):
                plugin = self._import_path(path[:-3])
                if plugin:
                    self.days.append(plugin)

    def _is_plugin_path(self, path: str) -> bool:
        """Returns if the path is a plugin"""
        return path.endswith(".py") and path != '__init__.py'

    def _import_path(self, day) -> RunDay:
        """Imports a day if there are no errors happening."""
        try:
            plugin = importlib.import_module(f'solutions.year_2021.days.{day}').Day()
        except ImportError:
            plugin = None

        if isinstance(plugin, RunDay):
            return plugin

    def run_days(self) -> None:
        """Run all days."""
        for plugin in self.days:
            plugin.run()

    def run_latest(self) -> None:
        """Run the last day, for working on the latest solution."""
        self.days[-1].run()

    def run_single_day(self, day) -> None:
        """Runs a single advent of code day."""
        self.days[day-1].run()


def main():
    """Run the main function"""
    aoc = RunYears()
    aoc.run_days()


if __name__ == '__main__':
    main()
