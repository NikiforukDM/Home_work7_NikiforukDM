from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Can clean folders',
      url='https://https://github.com/NikiforukDM/home-work6/blob/main/%D0%94%D0%976.py',
      author='Nykyforuk Dmytro',
      author_email='NikiforukDM@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean_folder']})
