第一次：
	1、实现执行excel中用例，并进行测试结果回写
	2、实现路径常量化
	3、实现环境可配置
第二次：
	1、增加unittest框架，实现ddt数据驱动加载
	2、增加log日志打印
	3、实现数据库连接、获取手机号并进行处理后重写
	遗留问题：
	1、当手机号数据重写后，使用${}变量就被替换了，应该写的时候又加上？那读的时候又要去掉
	2、代码优化地方：
	    1、将testsuite和main模块封装好，放在setup中执行
	    2、思考日志加载哪里，加载日志的内容
	    3、思考那些地方需要封装
	    4、优化模块位置之前的关系，感觉放的有点乱
第三次：
    1、优化测试用例：删除url中冗余部分，采用配置文件拼接    --完成
    2、删除main函数中用例回写，在testcase执行时就进行回写，减少一次函数调用
    3、实现充值接口用例
    4、将回写测试结果和回写测试返回数据优化成一个函数       --完成
    5、优化配置文件获取方式
    6、进行模块分离化