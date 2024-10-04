import { SfeirThemeInitializer } from '../web_modules/sfeir-school-theme/sfeir-school-theme.mjs';

// One method per module
function schoolSlides() {
  const directory = '00-school/';
  return [
    //
    `${directory}00-TITLE.md`, //
    `${directory}speaker-cba.md`, //
    `${directory}speaker-bma.md`, //
    `${directory}01-intro.md`, //
  ]
}

function iaSlides() {
  const directory = '10-ia/';
  return [
    //
    `${directory}00-TITLE.md`, //
    ...breakSlide(),
  ]
}

function langchainSlides() {
  const directory = '20-langchain/';
  return [
    //
    `${directory}00-TITLE.md`, //
    `${directory}01-Presentation.md`, //
    `${directory}02-Basics.md`, //
    `${directory}03-DataLoading.md`, //
    `${directory}04-StoringData.md`, //
    `${directory}05-Advanced.md`, //
  ]
}

function applicationsSlides() {
  const directory = '30-applications/';
  return [
    //
    `${directory}00-TITLE.md`, //
    ...breakSlide(),
  ]
}

function toolsSlides() {
  const directory = '40-tools/';
  return [
    //
    `${directory}00-LangServe.md`, //
    `${directory}01-LangGraph.md`, //
    `${directory}02-LangSmith.md`, //
  ]
}

function concluSlide() {
  return ['98-conclusion.md'];
}
function breakSlide() {
  return ['99-break.md'];
}

function formation() {
  return [
    //
    ...schoolSlides(), //
    ...iaSlides(), //
    ...langchainSlides(), //
    ...applicationsSlides(), //
    ...toolsSlides(), //
    ...concluSlide(), //
  ].map((slidePath) => {
    return { path: slidePath };
  });
}

SfeirThemeInitializer.init(formation);
