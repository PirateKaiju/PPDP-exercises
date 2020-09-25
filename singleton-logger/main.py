import mylogger

test_logger = mylogger.Logger()

print(test_logger)
test_logger.error("This is an error")
test_logger.error("This is another error")
test_logger.warning("This is a warning")

maybe_another_logger = mylogger.Logger()
print(maybe_another_logger)

test_logger = mylogger.Logger()
test_logger = mylogger.Logger()
print(test_logger)