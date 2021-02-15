/**
 * Find and fix bibliographic citations.
 * @param {string} toRoot Path to root of volume.
 */
const fixBibCites = (toRoot) => {
  Array.from(document.querySelectorAll('cite'))
    .forEach(node => {
      const keys = node.innerHTML
            .trim()
            .split(',')
            .map(key => key.trim())
            .map(key => `<a href="${toRoot}/bibliography/#${key.toLowerCase()}">${key}</a>`)
            .join(', ')
      const cite = document.createElement('span')
      cite.innerHTML = `[${keys}]`
      node.parentNode.replaceChild(cite, node)
    })
}

/**
 * Find and fix glossary references.
 * @param {string} toRoot Path to root of this volume.
 * @param {string} volume Name of this volume.
 */
const fixGlossaryRefs = (toRoot) => {
  Array.from(document.querySelectorAll('g'))
    .forEach(node => {
      const key = node.getAttribute('key')
      const link = document.createElement('a')
      link.setAttribute('href', `${toRoot}/glossary/#${key}`)
      link.setAttribute('class', 'glossary-reference')
      link.innerHTML = node.innerHTML
      node.parentNode.replaceChild(link, node)
    })
}

/**
 * Perform all in-page fixes.
 */
const fixPage = () => {
  const toRoot = '..'
  fixBibCites(toRoot)
  fixGlossaryRefs(toRoot)
}
