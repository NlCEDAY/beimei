方法栈中有指针指向堆的对象

A a = new A() a就为引用对象指向A（）

new操作会产生2个对象

栈里放--引用对象和基本类型：

基本类型有长度限制，不需要放在堆里，堆里不确定大小的对象放的，直接放在方法栈里

方法区里放方法名字引用

![image-20200624100643926](C:%5CUsers%5Clenovo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200624100643926.png)

方法有局部变量，

反射作为**类型信息拿对象属性**，通过（属性.对象,方法.对象）的方式来反过来**动态获取**，

