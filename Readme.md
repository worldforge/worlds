# Worldforge Worlds

This is a collection of worlds for the [Worldforge](http://www.worldforge.org/) system. They are meant to be imported into a running [Cyphesis](https://github.com/worldforge/cyphesis) server using either the `cyimport` console command, or the [Ember](https://github.com/worldforge/ember) client.
The worlds are organized by rulesets. The current default ruleset of Cyphesis is "Deeds".

If you want to build and run a server yourself we recommend using the [Hammer](https://github.com/worldforge/hammer) tool.

For licensing see the file COPYING.

## Importing worlds

Use the `cyimport` command to import worlds into a running instance of Cyphesis.
```
cyimport deeds/braga/world.xml
```

If you want to start with a new world you can use the ```--clear``` option, which will wipe any existing world.
For example
```
cyimport --clear deeds/empty_island/world.xml
```

## Exporting worlds

Use the `cyexport` command to export worlds from a running instance of Cyphesis.
```
cyexport deeds/braga/world.xml
```
