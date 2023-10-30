import os

from conan import ConanFile
from conan.tools.files import copy


class Conan(ConanFile):
    name = "worldforge-worlds"
    version = "0.1.0"
    author = "Erik Ogenvik <erik@ogenvik.org>"
    url = "https://github.com/worldforge/worlds"
    homepage = "https://www.worldforge.org"
    description = "A collection of worlds for the Worldforge system."
    topics = ("mmorpg", "worldforge")
    user = "worldforge"
    package_type = "header-library"

    # No settings/options are necessary, this is header only
    exports_sources = ["deeds/*", "mason/*"]
    no_copy_source = True

    def package(self):
        copy(self, "*", self.source_folder, os.path.join(self.package_folder, "worlds"))
