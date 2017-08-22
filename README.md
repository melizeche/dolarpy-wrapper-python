# dolarpy-wrapper-python

API wrapper for DolarPy https://dolar.melizeche.com
https://github.com/melizeche/dolarPy

## Install

```
pip install dolarpy
```

## Usage
```
import dolarpy

providers = dolarpy.get_providers() # 'bcp', 'maxicambios', 'cambioschaco', etc...
dolar_referencial = dolarpy.get() # default: BCP referencial_diario
dolar_compra_chaco = dolarpy.get_compra(provider='cambioschaco')
dolar_venta_maxi = dolarpy.get_venta(provider='maxicambios')

```

## Requirements

- Python 2.7 or 3+
- requests==2.18.4


## Dev Instructions
```
- git clone
- virtualenv env
- source env/bin/activate
- pip install -r requirements.txt
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## TODO

* Testing
* ~~Proper~~ Extend documentation
* More API methods

## Credits

* Marcelo Elizeche Landó

## License

This project is licensed under the terms of the MIT license - see the [LICENSE](LICENSE) file for details
