A tool to find differences between two iTunes Music libraries. Why would I need a differ for that? Well, clearly you've never deleted songs from iTunes with Apple Music enabled and were surprised that there is no way to undo that or see recently deleted songs. Here's how I saved my weekend:

- Fetch your old `iTunes Music Library.xml` from your backup.
- Use `itunesdiff` to compare what songs where removed and added.
- Add those songs manually again

```bash
itunesdiff wednesday.xml saturday.xml --albums

< Firewatch Original Score - Chris Remo
< Columbus - Hammock
> Hurry Up, We're Dreaming - M83
> My Best Human Face - Moonface & Siinai
> Julia With Blue Jeans On - Moonface
```

# Usage

```
usage: itunesdiff [-h] [-a] xmlfiles xmlfiles

Diffs two iTunes XML files.

positional arguments:
  xmlfiles      Path to two iTunes XML files

optional arguments:
  -h, --help    show this help message and exit
  -a, --albums  Diff albums only
```
