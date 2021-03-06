from setuptools import setup, find_packages, Extension
import sys

extensions = []

extensions.append(Extension("Adafruit_DHT.Raspberry_Pi_2_Driver",
                            ["source/_Raspberry_Pi_2_Driver.c", "source/common_dht_read.c", "source/Raspberry_Pi_2/pi_2_dht_read.c", "source/Raspberry_Pi_2/pi_2_mmio.c"],
                            libraries=['rt'],
                            extra_compile_args=['-std=gnu99']))


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

# Call setuptools setup function to install package.
setup(name              = 'Adafruit_DHT',
      version           = '1.3.2',
      author            = 'Tony DiCola',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Library to get readings from the DHT11, DHT22, and AM2302 humidity and temperature sensors on a Raspberry Pi or Beaglebone Black.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/iZonex/Adafruit_Python_DHT/',
      packages          = find_packages(),
      ext_modules       = extensions)
