# LeetCode Python 

欢迎使用 LeetCode Python 模版！

[github](https://github.com/zonewave/leetcode-precompiled)

## 适用情况
当直接上手写solution，无法通过测试用例时，再使用此模板来进行调试
## pycharm 本地环境配置

### 1. 安装[leetcode-editor](https://github.com/shuzijun/leetcode-editor)
安装后，请注意检查生成的代码路径
### 2. [安装工具库](https://github.com/zonewave/leetcode-precompiled/tree/master/py)

### 3. 配置模板

![settingimag](./img/templatesetting.jpg)

[模板一](./jetbrain_editor_template.md)
这里除了最后的几行以外， import部分 都是官方web实际运行导入的库

[模板二，推荐](./jetbrain_editor_template2.md)
与模板一不同，这个主要简化了import，可以直接全量导入库，第一个是为了某些时候按需导入其他库，新手默认推荐这个。

## pycharm 本地调试
点击题目，配置好用例，然后进行运行或者调试
### 动图演示
![init](https://pic.imgdb.cn/item/67078defd29ded1a8c98f822.gif)
看不到gif，请看[这里](https://pic.imgdb.cn/item/67078defd29ded1a8c98f822.gif)


## vscode 本地调试步骤

可以直接clone 本项目，然后打开py文件夹即可加载部分配置。
或者也可以复制本目录下的/.vscode 文件夹 文件到到自己项目的.vscode也可。
### 1. 安装官方扩展并配置 Leetcode

参考官方的说明，配置好账号密码，这里就不说明

### 2. 代码路径的配置

settings里搜索leetcode,在filepath 那块 打开setting.json,用下面的配置，添加或者替换Python3的文件路径声明

```json
{
  "leetcode.filePath": {
    "python3": {
      "folder": ".",
      "filename": "test_${id}_${snake_case_name}.py"
    }
  },
  "leetcode.useEndpointTranslation": false,
}
```

### 3. [安装工具库](https://github.com/zonewave/leetcode-precompiled/tree/master/py)(可选)

### 4. 生成代码片段

点击lc界面里任一题目生成文件后，在空白处，敲击lctest，然后使用tab自动补全，接着像pycharm 那样填参数即可

### 5. 配置unittest测试并断点调试

本模板用的是uniittest框架。
vscode的测试配置，参考微软的[文档](https://vscode.github.net.cn/docs/python/testing#_configure-tests)
写好答案后，点击test界面，运行即可

#### 动图演示

看不到gif，请看[这里](https://pic.imgdb.cn/item/67092251d29ded1a8cd5a53a.gif)
![运行](https://pic.imgdb.cn/item/67092251d29ded1a8cd5a53a.gif)


```  
