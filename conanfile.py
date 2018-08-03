from conans import ConanFile, CMake, tools

class AgnesConan(ConanFile):
    name = "Agnes"
    version = "0.1"
    license = "MIT"
    
    description = "AnnotationGenerator conan package"
    settings = "os", "compiler", "build_type", "arch"
    description = "AnnotationGenerator conan AnnotationG"
    generators = "cmake"
    exports_sources = ["Modules/*", "Dependencies/*", "Source/*", "CMakeLists.txt"]

    def conan_info(self):        
        self.info.include_build_settings()
        del self.info.settings.compiler
        del self.info.settings.arch
        del self.info.settings.build_type

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/Reflection", src="Source/Reflection/include")

        if self.settings.os == "Windows":
            self.copy("Agnes.exe", dst="bin", src="Source/Preprocessor/Release", keep_path=False, ignore_case=True)
        else:
            self.copy("Agnes", dst="bin", src="Source/Preprocessor", keep_path=False, ignore_case=True)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self, folder="lib");
