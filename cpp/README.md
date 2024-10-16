# LeetCode cpp 
欢迎使用 LeetCode cpp  模版




## 效果显示
看不到gif，请看[这里](https://pic.imgdb.cn/item/670ccfcdd29ded1a8cd9f738.gif)
![vscode](https://pic.imgdb.cn/item/670ccfcdd29ded1a8cd9f738.gif)

## 本地环境配置说明
可以直接把项目 git clone 下来，然后用vscode/clion/其他ide 切到cpp文件夹，即可使用
或者把本项目的 cmakelist.txt,test_sources.cmake.in, common(通用的cpp代码块), .vscode里的文件（如果使用到vscode）话， 复制到自己项目里，也可使用。

主要思路是把每个需要solution代码纳入到测试体系.
由于cpp标准库里没啥好用的测试工具，所以使用doctest（这是个超轻量的，并且很流行的库）了来进行测试运行。

本项目需要包管理工具 ，这里使用cmake(后续可能会给xmake,hunter,conan之类的)，vscode,clion 都支持cmake的解析。

### 目录结构说明
```
project/
    .vscode
    cmake-build-debug  #构建目录，也可以用build做构建目录名
    cn/  #中文站点
      test_1_two_sum.cpp #解题代码
      ...
    en/ 
      test_1_two_sum.cpp #解题代码
      ...
    common/    #通用目录
    CMakeLists.txt  #cmake 文件

```
导入项目配置后，第一次先build，保证build成功。

**注意：一般简单题，可以不需要单步调试就能解决，直接导个头文件，再写答案，最后用官方插件提交到网站就行了
只有你始终通不过的case再进行调试，效果可能会好点**

### 集成到测试构建
编写测试 的同时，在cmakelists.txt文件里这块添加cpp文件路径（因为cmake要指明哪些cpp文件要参与编译运行）。
```cmake
set(TEST_SOURCE_FILES
    #cn/test_1_two_sum.cpp
    #cn/test_2_add_two_numbers.cpp

    cn/???.cpp # add want test cpp
)
```

### 使用建议
一般情况，可能不需要单步调试就能解决，所以像上面那样只把需要测试的cpp文件加入到build过程中，


## vscode 

### vscode 插件和本地配置
vscode cpp配置 对新手来说，会比较麻烦，但请按下面一步步走.
#### 1. 安装官方扩展LeetCode 并配置 

参考官方的说明，配置好账号密码

#### 2. 安装c++,cmake tool,cmake,c++ testMate 四个扩展

vscode 默认build目录名 是build
如果需要换个build 目录，比如cmake-build-debug，需要改两个地方
设置里 搜索cmake-tools，设定构建目录为 ${workspaceFolder}/cmake-build-debug
![builddir](./img/builddir.png)

设置里 搜索testmate，在 excutables 配置 添加 cmake-build-debug

![testmatedir](./img/testmatedir.png)


#### 3. 代码路径的配置
settings里搜索leetcode,在filepath 那块打开setting.json,用下面的配置，添加或者替换cpp的文件路径声明

```json
{
  "leetcode.filePath": {
    // 这个是solution的cpp 文件的生成路径
    "cpp": {
      "folder": "cn", //英文站点就用en
      "filename": "test_${id}_${snake_case_name}.cpp"
    }
  },
  // 这个是禁用官方插件的翻译，否则会生成中文名的cpp文件。（其实中文名的，也能编译运行，就是容易调失败）
  "leetcode.useEndpointTranslation": false
}
```

#### 4. [安装工具库][https://github.com/zonewave/leetcode-precompiled/blob/master/cpp]
写链表，树，嵌套数组时所需的工具库，也可以不安装，自己在common文件里用你自己写的。


### vscode 进行调试



#### 1. 生成代码片段
**注意：一些简单题不写测试的话，这里导个common头文件,就可以跳过了**

点击lc界面里任一题目生成文件后，cmakelists.txt文件在[上文](#集成到测试构建)那提到的添加新生成的cpp文件路径。
在    // @lc code=start 上头空白处 ，敲击lctesth，然后使用tab自动补全，导入头文件和声明命令空间，这里命令空间写题号即可。
在// @lc code=end 下面空白处，敲击lctestb，然后使用tab自动补全，接着补充参数，填写用例。
然后在cmakelists.txt

#### 2. 配置测试


编写完测试用例后，需要通过命令面板，执行命令 cmake: build，构建测试。
构建之后，界面会出现三角绿色按钮，设置断点，右键即可运行调试。也可以在侧边栏cmake点击debug调试。


## clion 
clion 配置比较简单，只要把 leetcode插件安装好.
设置(在clion的settings.Tool.Leetcode Plugin或者侧边栏里leetcode tab里有个设置按钮)
leetcode插件里的文件夹路径，接着复制[模板](./tmpl/jetbrains_tmpl.md)里对应的code filename 和 code template就好了。

不需要调试的时候，把生成的test相关代码注释掉即可。
需要调试的时候，cmakelists.txt文件在[上文](#集成到测试构建)那提到的添加新生成的cpp文件路径。然后填写测试用例后，界面就有绿色按钮出现，这就可以进行运行和调试了。

### 动图演示
看不到gif，请看[这里](https://pic.imgdb.cn/item/670ccee5d29ded1a8cd8d5be.gif)
![clion](https://pic.imgdb.cn/item/670ccee5d29ded1a8cd8d5be.gif)



