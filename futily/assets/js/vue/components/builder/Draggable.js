import Sortable from 'sortablejs'

const props = {
  options: Object,
  list: {
    type: Array,
    required: false,
    default: null
  },
  clone: {
    type: Function,
    default: (original) => { return original }
  }
}

export default {
  props,

  render (h) {
    return h('div', null, this.$slots.default)
  },

  mounted () {
    const optionsAdded = {}

    for (const elt of ['Start', 'Add', 'Remove', 'Update', 'End']) {
      optionsAdded[ `on${elt}` ] = delegateAndEmit.call(this, elt)
    }

    for (const elt of ['Choose', 'Sort', 'Filter', 'Move', 'Clone']) {
      optionsAdded[ `on${elt}` ] = emit.bind(this, elt)
    }

    const options = merge(this.options, optionsAdded)
    this._sortable = new Sortable(this.$el, options)
  },

  beforeDestroy () {
    this._sortable.destroy()
  }
}

function emit (evtName, evtData) {
  this.$emit(evtName.toLowerCase(), evtData)
}

function delegateAndEmit (evtName) {
  return (evtData) => {
    emit.call(this, evtName, evtData)
  }
}

function merge (target, source) {
  const output = Object(target)

  for (const nextKey in source) {
    if (source.hasOwnProperty(nextKey)) {
      output[ nextKey ] = source[ nextKey ]
    }
  }

  return output
}
