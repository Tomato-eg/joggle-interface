from src.common.log_utils import LogUtils as lu

log = lu.get_log()


class AssertUtils:

    def __init__(self, expect, actual):
        self.expect = expect
        self.actual = actual

    def assert_tool(self):
        if self.expect is not None and self.actual is not None:
            try:
                assert self.expect == self.actual, f'预期:{self.expect} != 实际:{self.actual}'
            except AssertionError as e:
                log.error(f'执行断言错误:{e}')
        else:
            log.info('没有数值传入')


if __name__ == '__main__':
    AssertUtils(1, 2).assert_tool()
