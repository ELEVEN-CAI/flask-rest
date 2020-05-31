# coding:utf-8


class ExcelUtil(object):

	def __int__(self):
		self.content = None

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if all([exc_type, exc_val, exc_tb]):
			print('error')
		return True

	@staticmethod
	def read_content(dir_path):
		with open(dir_path, 'r') as f:
			return f.read()

	def task(self):
		pass


if __name__ == '__main__':
	with ExcelUtil() as eu:
		eu.task()

