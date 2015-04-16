# -*- coding: utf-8 -*-
"""
.. module:: convert_ESRF.py
   :platform: Unix
   :synopsis: Convert ESRF edf files in data exchange.

Example on how to use the `xtomo_raw`_ module to read ESRF edf raw tomographic data and save them as Data Exchange

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15

.. _xtomo_raw: dataexchange.xtomo.xtomo_importer.html
"""

# Data Exchange: https://github.com/data-exchange/data-exchange
import dataexchange

def main():

    file_name = '/media/DISK_02/databank/templates/esrf_ID19/tomo.edf'
    dark_file_name = '/media/DISK_02/databank/templates/esrf_ID19/dark.edf'
    white_file_name = '/media/DISK_02/databank/templates/esrf_ID19/flat.edf'
    hdf5_file_name = '/media/DISK_02/databank/templates/dataExchange/tmp/ESRF.h5'

    sample_name = 'edf test'


    # Read raw data
    read = dataexchange.Import()
    data, white, dark, theta = read.xtomo_raw(file_name,
                                                       white_file_name = white_file_name,
                                                       dark_file_name = dark_file_name,
                                                       data_type='edf',
                                                       log='INFO'
                                                       )

    # Save data as dataExchange
    write = dataexchange.Export()
    write.xtomo_exchange(data = data,
                          data_white = white,
                          data_dark = dark,
                          theta = theta,
                          hdf5_file_name = hdf5_file_name,
                          sample_name = sample_name,
                          data_exchange_type = 'tomography_raw_projections'
                          )

if __name__ == "__main__":
    main()

