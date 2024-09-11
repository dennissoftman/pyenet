# pyenet

pyenet is a python wrapper for the ENet library by Lee Salzman,
 http://enet.bespin.org

It was originally written by Scott Robinson <scott@tranzoa.com> and is
currently maintained by Andrew Resch <andrewresch@gmail.com>

## License
pyenet is licensed under the BSD license, see LICENSE for details.
enet is licensed under the MIT license, see http://enet.bespin.org/License.html

## Dependencies

Building pyenet requires all the same dependencies as enet plus Cython and,
obviously, Python.

## Installation

Just run
```
pip install enet-py
```

## Building

Obviously
```
python setup.py build
python setup.py install
```

## Usage

Once you have installed pyenet, you only need to import the enet module to
start using enet in your project.

Example server:
```py
>>> import enet
>>> host = enet.Host(enet.Address("localhost", 33333), 1, 0, 0)
>>> event = host.service(0)
```
Example client:
```py
>>> import enet
>>> host = enet.Host(None, 1, 0, 0)
>>> peer = host.connect(enet.Address("localhost", 33333), 1)
```
More information on usage can be obtained from:
 http://enet.bespin.org/Tutorial.html
