#include <stdio.h>
#include <wiringPi.h>

#define GPIO1  1

int main()
{
        int cmd;
        if(wiringPiSetup() == -1)// 硬件初始化
        {   
                printf("硬件初始化失败!\n");
                return -1;
        }
        pinMode(GPIO1, OUTPUT);   // 配置引脚的 IO 模式，此处我们连接了树莓派 GPIO.7，配置 7 号引脚为输出模式

        while(1){
        
                printf("请输入0或1，0--断开，1--闭合:\n");
                scanf("%d",&cmd);

                if(cmd == 0){
                        digitalWrite(GPIO1, HIGH);   // 引脚 GPIO.7 输出高电平
                        printf("开关断开！\n");
                }else if(cmd == 1){
                        digitalWrite(GPIO1, LOW);   // 引脚 GPIO.7 输出低电平
                        printf("开关闭合！\n");
                }else{
                        printf("输入错误，");
                }
        }

        return 0;
}
