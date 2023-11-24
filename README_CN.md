# Micropython 库

## 目录介绍

  目录library为各种传感器的库文件，可以使用带有micropython固件的板子进行使用，需要手动将库文件上传到板子上，后续我们定制的固件会自动内置这些库文件，方便使用。

  目录examples下面的各个main.py为library的示例参考代码，可以直接上传到板子上运行。

## 快速开始

- 首先需要有一块带micropython的固件的esp32板子，可以参考官方文档进行下载烧录：[https://micropython.org/download/ESP32_GENERIC/](https://micropython.org/download/ESP32_GENERIC/)，建议直接下载最新稳定的v1.21.0版本: [**v1.21.0 (2023-10-05) .bin**](https://micropython.org/resources/firmware/ESP32_GENERIC-20231005-v1.21.0.bin)

- 烧录完成后，电脑打开任一串口工具，选择板子对应的USB端口并把波特率设置为115200, 板子重启可以看到串口工具正常打印micropython的版本信息，就代表烧录完成并成功运行，如下所示:

  ```text
  MicroPython v1.21.0-3 on 2023-11-22; Generic ESP32 module with ESP32
  Type "help()" for more information.
  >>>
  ```

## 上传文件

- 给micropython上传文件的命令行工具和图形化工具很多，如果你不知道使用哪种，可以使用命令行工具adafruit-ampy，查看[官方文档](https://pypi.org/project/adafruit-ampy/)进行安装使用

- ampy会使用串口，所以在使用ampy之前需要停止串口工具程序，然后可以使用如下命令查看一下esp32的文件，验证ampy是否可以正常使用，例如现在esp32在windows上连接的是COM1端口，那么查看指令如下:

```shell
ampy -p COM1 ls
```

  运行正常列出 */boot.py* 等文件

## 调试示例与库

这里以无源蜂鸣器为例，对应的库为**library\buzzer.py**, 先将库文件上传到板子中:

```shell
ampy -p COM1 put library\buzzer.py
```

再上传一个buzzer示例文件作为主程序：例如**examples\buzzer\play_a_melody\main.py**:

```shell
ampy -p COM1 put examples\buzzer\play_a_melody\main.py
```

上传完成重启板子，会自动运行main.py，这样就成功运行了一个示例程序

每个示例程序的说明可以查看examples中每个main.py文件本身的注释
