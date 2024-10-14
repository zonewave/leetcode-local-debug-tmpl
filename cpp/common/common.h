#ifndef COMMON_H
#define COMMON_H

#include "doctest.h"
#include "precompiled/headers.h"
using namespace std;

template <typename... Args>
struct ArgsHolder
{
    std::tuple<Args...> args; //

    ArgsHolder(Args... args) : args(make_tuple(std::forward<Args>(args)...))
    {
    }

    template <size_t Index>
    auto get() const
    {
        return std::get<Index>(args);
    }
};

template <typename R, typename... Args>
struct LTestCase
{
    std::string name;
    ArgsHolder<Args...> args;
    R want;

    LTestCase(std::string name, R want, Args... args)
        : name(std::move(name)), args(args...), want(want)
    {
    }
};

#endif
