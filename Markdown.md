### Markdown语法
> 互联网之子(电影)

1. 标题
'#' 一级标题
'##' 二级标题
'###' 三级标题
'####' 四级标题
'#####' 五级标题
'######' 六级标题
2. 列表
无序列表:
'*'
'+'
'-'
有序列表:
'1'
'2'
3. 链接
行内链接:'[链接文字](链接地址)'
页内跳转:```[名称](#id)```
        ```<a href="#id">名称```
4. 强调
' * ' 强调内容 ' * '
' _ ' 强调内容 ' _ '
' ** ' 加粗特效 ' ** '
' __ ' 加粗特效 ' __ '
5. 自动生成目录
* pandoc -s --toc xxx.md -o xxx.md(需要安装pandoc)
* Visual Studio Code中的Markdown TOC扩展
* doctoc xx.md
6. 一些插件
minimap ----类似于sublim text右边的代码缩略图
atom-beautify
autocomplete-paths 路径提示
pigments 颜色背景显示
color-picker 取色器  
