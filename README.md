# About (Part to remove)

Template repository for SFEIR School, this template could be use to start a school with revealJS and SFEIR School theme

Don't forget to replace all xxx by your techno

## Files to changes

- `docs/scss/slides.scss` you could put here all your custom styles
- `docs/scripts/slides.js` you will reference all the markdown here. Don't forget to have 1 function per chapter (module).
- `docs/index.html` you should reference the correct technology in header

## To helps you

Video to help you to create your slides with revealJS

[![video of how to do a sfeir school](https://img.youtube.com/vi/v4WuJIwf4lc/0.jpg)](https://www.youtube.com/watch?v=v4WuJIwf4lc)

You could also look at documentation of school theme : https://github.com/sfeir-open-source/sfeir-school-theme

## Tasks to do

- [] Change the files (cf before)
- [] Replace all xxx by your techno
- [] Remove this part of README
- [] Complete the README with your content
- [] Check that the github pages is pointing to `/docs` directory

# Content of README

The text below is the template you could use for your readme

# SFEIR School XXX

<p align="center">
 <img style="display:block" width="20%" height="20%" src="./docs/assets/images/sfeir-school-logo.png" alt="SFEIR School logo">
</p>

<br/>

[Discover the SFEIR Schools](https://www.sfeir.com/fr/le-contenus-dexperts-de-la-technologie-et-de-linnovation/formation-gratuite-avec-nos-experts/)

# Slides

You can view the slides [here](https://sfeir-open-source.github.io/sfeir-school-xxx/).

## Develop

To run docs locally, go in directory `docs` and run `npx serve` of if you don't have node, you can use docker `docker-compose up`, and open slides on http://localhost:3000/.

## Workshop

Workshops are in directory `steps` :

- two directories per workshop :
  - one with a README.md with workshop steps and source file to complete
  - a second directory suffixed with `-solution` which contains source file with solutions.

## Contributing

### Contributing Guidelines

Read through our [contributing guidelines][contributing] to learn about our submission process, coding rules and more.

### Want to Help?

Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our guidelines for [contributing][contributing] and then check out one of our issues labeled as <kbd>help wanted</kbd> or <kbd>good first issue</kbd>.

### Code of Conduct

Help us keep Angular open and inclusive. Please read and follow our [Code of Conduct][codeofconduct].

[contributing]: CONTRIBUTING.md
[codeofconduct]: https://github.com/sfeir-open-source/code-of-conduct/blob/master/CODE_OF_CONDUCT.md
