#include <Constants.au3>


ControlSetText("选择要加载的文件", "", "[ID:1148]", $CmdLine[1])

ControlClick("选择要加载的文件", "", 1)
