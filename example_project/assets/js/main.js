import 'babel-polyfill'
import 'utils/class-list-polyfill'
import 'utils/focus-ring'

import { svg4everybody } from './utils/svgforeverybody'

import { Navigation } from './site'
import LazyImage from './utils/lazy-image'
import { externalLinks, iframeFix } from './utils'

document.addEventListener('DOMContentLoaded', () => {
  const body = document.body || document.documentElement
  body.classList.add('util-JSEnabled')

  externalLinks()
  new Navigation()

  const lazyImage = document.querySelector('.js-LazyImage')
  if (lazyImage) {
    const lazyImages = document.querySelectorAll('.js-LazyImage')
    Array.from(lazyImages).map(image => new LazyImage({ el: image }))
  }

  // If the browser isn't Safari, don't do anything
  if (
    document.querySelector('iframe') &&
    window.navigator.userAgent.indexOf('Safari') > -1
  ) {
    iframeFix()
  }

  // If the device is iOS add a class to the body so we can do specific CSS for it
  if (!!navigator.platform && /iPad|iPhone|iPod/.test(navigator.platform)) {
    const body = document.body || document.documentElement
    body.classList.add('is-iOS')
  }

  svg4everybody()

  // This class is used for making the animation duration on CSS animations 0, initially
  setTimeout(() => {
    document.body.classList.remove('util-Preload')
  }, 500)
})
