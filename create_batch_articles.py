from mysql.connector import pooling
import random
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from pymysql import escape_string

cnxpool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=32, user='root', password='123456',
                                      host='localhost', database='mycms')

################
# 文章内容
article_template = '''
What’s New In Python 3.8
Editor
Raymond Hettinger
This article explains the new features in Python 3.8, compared to 3.7. For full details, see the changelog.
Python 3.8 was released on October 14th, 2019.
Summary – Release highlights
New Features
Assignment expressions
There is new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus.
In this example, the assignment expression helps avoid calling len() twice:
if (n := len(a)) > 10: print(f"List is too long ({n} elements, expected <= 10)")
A similar benefit arises during regular expression matching where match objects are needed twice, once to test whether a match occurred and another to extract a subgroup:
discount = 0.0
if (mo := re.search(r'(\d+)% discount', advertisement)):
discount = float(mo.group(1)) / 100.0
The operator is also useful with while-loops that compute a value to test loop termination and then need that same value again in the body of the loop:
# Loop over fixed length blocks
while (block := f.read(256)) != '':process(block)
Another motivating use case arises in list comprehensions where a value computed in a filtering condition is also needed in the expression body:
[clean_name.title() for name in names
if (clean_name := normalize('NFC', name)) in allowed_names]
Try to limit use of the walrus operator to clean cases that reduce complexity and improve readability.
See PEP 572 for a full description.
(Contributed by Emily Morehouse in bpo-35224.)
Positional-only parameters
There is a new function parameter syntax / to indicate that some function parameters must be specified positionally and cannot be used as keyword arguments. This is the same notation shown by help() for C functions annotated with Larry Hastings’ Argument Clinic tool.
In the following example, parameters a and b are positional-only, while c or d can be positional or keyword, and e or f are required to be keywords:
def f(a, b, /, c, d, *, e, f):print(a, b, c, d, e, f)
The following is a valid call:
f(10, 20, 30, d=40, e=50, f=60)
However, these are invalid calls:
f(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
f(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument
One use case for this notation is that it allows pure Python functions to fully emulate behaviors of existing C coded functions. For example, the built-in pow() function does not accept keyword arguments:
def pow(x, y, z=None, /):
"Emulate the built in pow() function"r = x ** y
return r if z is None else r%z
Another use case is to preclude keyword arguments when the parameter name is not helpful. For example, the builtin len() function has the signature len(obj, /). This precludes awkward calls such as:
len(obj='hello')  # The "obj" keyword argument impairs readability
A further benefit of marking a parameter as positional-only is that it allows the parameter name to be changed in the future without risk of breaking client code. For example, in the statistics module, the parameter name dist may be changed in the future. This was made possible with the following function specification:
def quantiles(dist, /, *, n=4, method='exclusive')
Since the parameters to the left of / are not exposed as possible keywords, the parameters names remain available for use in **kwargs:
This greatly simplifies the implementation of functions and methods that need to accept arbitrary keyword arguments. For example, here is an excerpt from code in the collections module:
Parallel filesystem cache for compiled bytecode files
The new PYTHONPYCACHEPREFIX setting (also available as -X pycache_prefix) configures the implicit bytecode cache to use a separate parallel filesystem tree, rather than the default __pycache__ subdirectories within each source directory.
The location of the cache is reported in sys.pycache_prefix (None indicates the default location in __pycache__ subdirectories).
(Contributed by Carl Meyer in bpo-33499.)
Debug build uses the same ABI as release build
Python now uses the same ABI whether it’s built in release or debug mode. On Unix, when Python is built in debug mode, it is now possible to load C extensions built in release mode and C extensions built using the stable ABI.
Release builds and debug builds are now ABI compatible: defining the Py_DEBUG macro no longer implies the Py_TRACE_REFS macro, which introduces the only ABI incompatibility. The Py_TRACE_REFS macro, which adds the sys.getobjects() function and the PYTHONDUMPREFS environment variable, can be set using the new ./configure --with-trace-refs build option. (Contributed by Victor Stinner in bpo-36465.)
On Unix, C extensions are no longer linked to libpython except on Android and Cygwin. It is now possible for a statically linked Python to load a C extension built using a shared library Python. (Contributed by Victor Stinner in bpo-21536.)
On Unix, when Python is built in debug mode, import now also looks for C extensions compiled in release mode and for C extensions compiled with the stable ABI. (Contributed by Victor Stinner in bpo-36722.)
To embed Python into an application, a new --embed option must be passed to python3-config --libs --embed to get -lpython3.8 (link the application to libpython). To support both 3.8 and older, try python3-config --libs --embed first and fallback to python3-config --libs (without --embed) if the previous command fails.
Add a pkg-config python-3.8-embed module to embed Python into an application: pkg-config python-3.8-embed --libs includes -lpython3.8. To support both 3.8 and older, try pkg-config python-X.Y-embed --libs first and fallback to pkg-config python-X.Y --libs (without --embed) if the previous command fails (replace X.Y with the Python version).
On the other hand, pkg-config python3.8 --libs no longer contains -lpython3.8. C extensions must not be linked to libpython (except on Android and Cygwin, whose cases are handled by the script); this change is backward incompatible on purpose. (Contributed by Victor Stinner in bpo-36721.)
'''
titles = article_template.splitlines()[1:]
###
# # articles表
# create_articles = '''
# CREATE TABLE `articles2` (
#   `article_id` int(11) NOT NULL AUTO_INCREMENT,
#   `article_type` int(11) NOT NULL,
#   `title` char(255)  NOT NULL,
#   `content` text ,
#   `author` int(11) DEFAULT NULL,
#   `pub_date` datetime DEFAULT NULL,
#   `edit_date` datetime DEFAULT NULL,
#   PRIMARY KEY (`article_id`),
#   KEY `book_type_index` (`article_type`),
#   KEY `author_idx` (`author`),
#   CONSTRAINT `author` FOREIGN KEY (`author`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

# '''
# # 取出用户id，用于随机设定作者
cnx = cnxpool.get_connection()
cursor = cnx.cursor()
# cursor.execute(create_articles)
# cnx.commit()

user_ids_sql = "select user_id from users";
cursor.execute(user_ids_sql)
user_ids = cursor.fetchall()
cursor.close()
cnx.close()


def create_batch_articles():
    try:
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
    except:
        print("wait...")
        return

    sql_list = []
    sql = "INSERT INTO `mycms`.`articles` VALUES "
    # 每循环一次，生成10条文件
    for i in range(10):
        article = {
            "title": escape_string(random.choice(titles))[0:200],
            "content": escape_string("\r\n".join(random.choices(titles, k=random.randint(10, 20)))),
            "author": random.choice(user_ids)[0],
            "pub_date": datetime.now() - timedelta(days=random.randint(0, 300)),
            "edit_date": datetime.now()
        }

        values = "(null, 1, '{title}', '{content}', '{author}', '{pub_date}','{edit_date}')".format(**article)
        sql_list.append(values)
    try:
        sql += ",".join(sql_list)
        print(sql)
        cursor.execute(sql)
        cnx.commit()
    except Exception as e:
        print("error:", e)
    finally:
        cursor.close()
        cnx.close()


pool = ThreadPoolExecutor(30)
for i in range(10000):
    pool.submit(create_batch_articles)
