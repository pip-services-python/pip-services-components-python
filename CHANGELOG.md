# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> Component definitions for Python Changelog

## <a name="3.4.0"></a> 3.4.0 (2021-05-05)

### Bug fixes
* fixed names of private, protected and public properties and methods
* fixed interfaces method names
* fixed CompositeFactory.can_create

### Features
* added type hints
* CacheEntry added methods:
    - get_key
    - get_value
    - get_expiration
* fixed initialization of default factories and child classes
* Logger added get_source, set_source methods
* CacheCounter added get_interval, set_interval methods
* CachedLogger add max_cache_size param


## <a name="3.3.0"></a> 3.3.0 (2021-04-12)

### Features
* **trace** Added NullTracer class
* **trace** Added LogTracer class
* **trace** Added CachedTracer class
* **trace** Added CompositeTracer class
* Added tracer to Component class
* **connect** Added CompositeConnectionResolver class
* **connect** Added ConnectionUtils class

## <a name="3.2.2"></a> 3.2.2 (2021-03-08)

### Bug Fixes
* Logger fix %s strings

## <a name="3.2.1"></a> 3.2.1 (2020-12-24)

### Features
added **Test** module

## <a name="3.2.0"></a> 3.2.0 (2020-12-21)

### Features
added **Lock** module

### Breaking changes
* **ConfigReader** rename _read_config methods to _read_config

### Bug Fixes
* fixed Logger output args
* fixed imports


## <a name="3.1.1"></a> 3.1.1 (2020-08-01)
* Fixed issues

## <a name="3.0.0"></a> 3.0.0 (2018-10-30)

### New release
* Initial public release

### Features
- **Auth** - authentication credential stores
- **Build** - component factories framework
- **Cache** - distributed cache
- **Config** - configuration framework
- **Connect** - connection discovery services
- **Count** - performance counters components
- **Info** - context info
- **Log** - logging components