import Tagify from '@yaireo/tagify'
import '@yaireo/tagify/src/tagify.scss' // imports tagify SCSS file from within

let inputElement = document.querySelector('input')
new Tagify(inputElement)
