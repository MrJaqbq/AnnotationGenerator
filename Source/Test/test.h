
#include "inject.h"
#include <string>

namespace Core
{
    struct dunno {};
    namespace Utils {
        template <typename T>
        class sth
        {
            int theField;
        };
    }
}

namespace koza::kwas
{
    $YClass();
    enum MyEnum
    {
        None = 0,
        Sth = 1,
        Koza = 2,
        Default = Koza | Sth
    };

    class Attribute
    { };

    class Serialize : public Attribute
    {
        using test = Core::Utils::sth<Core::dunno>;

        test FunIsFun;

    public:
        std::string Name;
    };

    using AliasSerialize = Serialize;

    typedef Serialize TypedefSerialize;

    struct IsVocal : public Attribute
    { };

    struct Dupersznit : public Attribute
    { };

    $YClass(Serialize, IsVocal(true), Dupersznit{ 0, 1})
    $YClass(SomethingElse)
    class Meta(CTTI) TestYClass
    {

    };

    class Meta(Serialize) MyGreatClass
    {
        [[nodiscard]]
        auto sth() -> bool;

    public:
         MyGreatClass();
        ~MyGreatClass();

        MyGreatClass& operator==(const MyGreatClass&) = delete;
        MyGreatClass& operator==(MyGreatClass&&) = default;

        float Float;
        int*  pInt;

        Meta(Serialize)
        void ThePublic();

        int normalMethod(float f, bool* b);

        Core::dunno  byValue();
        Core::dunno* byPtr();
        Core::dunno& byRef();

        Core::Utils::sth<Core::dunno> getTemplate();
        void setTemplate(Core::Utils::sth<Core::dunno>& sth);

        template <typename T>
        void theTemplatedMethod(T* something);
    };

    // Surprise!
    int MyGreatClass::normalMethod(float f, bool* b)
    {

    }

    static_assert(true);
}
