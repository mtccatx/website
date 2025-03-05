## Hosting

So you'd like to host some content on the internet. You've come to the right
place! As a member of Moontower Computer Club, you have the awesome power of
making content available on world wide web :D

### Sounds good, let's get a nice landing page going!

*Anything* you put in `~/public` will be publically visible at `https://moontowercomputer.club/~<YOUR USERNAME>/`.
For example, if you had a picture called `selfie.jpg` and it was present at
`~/public/images/selfie.jpg`, you could also view the picture in your browser at:
`https://moontowercomputer.club/~<YOUR USERNAME>/images/selfie.jpg`. There are a
few exceptions:

+ Hidden files (files or directories whose name starts with `.`) will never be
  served. 
+ Anything in `public/cgi-bin/` is special. More on this below.

<details>
<summary>What's the deal with all the `~`(tilda)s?</summary>
`~` is shorthand for `/home/<YOUR USERNAME>`. Your shell should automatically
translate `~` to `/home/<YOUR USERNAME>` when it sees it. On the website we use
`/~<YOUR USERNAME>` as part of the URL mostly by convention.
</details>

First things first, you'll need to have set up your ssh access. Next you'll need
some kind of editor. You have two options here:

+ Edit files locally on your computer and copy them over to the server
+ Edit files directly on the server

For editing on the server itself, I recommend learning how to use `vim` (or
`neovim`), or at least becoming aware of `nano`. Both `vim` and `nano` are
preinstalled on `moontower`.

For editing locally, check out `vscode`'s `ssh` plugins. These let you run a
full graphical editor (`vscode`) locally, but it also enables remotely accessing
files on the server. Another option to use a graphical editor in this way is to
use `git` to synchronize changes across machines, and another other option is to
use `scp` or `rsync` for a similar affect.

You'll have to learn `HTML/CSS/JS` on your own\* (\*: we'll help you out, but
you need to poke around a little to find out what you need help with), but
here's a quick little starter pack:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My Homepage</title>
    </head>
    <body>
        <h1>Hello world!</h1>
        <p>This is my homepage!!!</p>
    </body>
</html>
```

#### Is all of this HTML really necessary???

No. You could also just do plain text, or you can also omit a lot of stuff and
it would still render mostly fine. For example, you could totally just do:

```html
<h1>Hello world!</h1>
This is my homepage!!!
```

And it would mostly look the same (sans the custom window title).

### CGI Scripts
