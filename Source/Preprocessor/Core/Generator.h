//
// Created by bentoo on 27.03.18.
//

#ifndef ANNOTATIONGENERATOR_GENERATOR_H
#define ANNOTATIONGENERATOR_GENERATOR_H

#include "Context.h"

class Generator
{
    using TTypeCache = std::map<std::string, TMustacheData>;

    Data::Context& Context;
    TTypeCache     Cache;

    TMustacheData BuildAllData      ();
    TMustacheData BuildTypeData     (std::shared_ptr<ClassInfo>& type);
    TMustacheData BuildFieldData    (std::shared_ptr<ClassInfo>& type);
    TMustacheData BuildMethodData   (std::shared_ptr<ClassInfo>& type);
    TMustacheData BuildAttributeData(std::shared_ptr<ClassInfo>& type);
    fs::path      BuildOutputPath   (std::shared_ptr<ClassInfo>& type);

public:
    explicit Generator(Data::Context& context);

    void GenerateFiles();
};


#endif //ANNOTATIONGENERATOR_GENERATOR_H
