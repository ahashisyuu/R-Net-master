from pip._internal import get_installed_distributions
from subprocess import call
for package in get_installed_distributions():
   call('pip install --upgrade' + package.project_name)

# 作者：小德子
# 链接：https://www.zhihu.com/question/63202629/answer/206646542
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。