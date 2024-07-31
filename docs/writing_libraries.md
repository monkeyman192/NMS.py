# Writing Libraries

The primary usage of *pyMHF* is to facilitate writing python libraries which can then be used to write mods.
*pyMHF* provides all the tools required to make setting up a library easy, so that one only has to provide the definitions and all the hooking and mod complexity will be handled automatically.

Follow the next steps to get your library project set up.

## Creating the folder structure

```
LibraryName
├── functions
│   ├── __init__.py
│   ├── call_sigs.py
│   ├── hooks.py
│   ├── offsets.py
├── types
│   ├── structs.py
├── __init__.py
└── pymhf.cfg
```