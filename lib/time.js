
function timeDiffToNow(d1Str){
    const d1 = new Date(d1Str)
    const d2 = Date.now()
    const diff = d2 - d1

    if (isNaN(diff)) return 'Not recently'
    // console.log('Raw diff', diff)
    const seconds = diff / 1000
    // const minutes = diff / 1000
    // const hours = diff / 1000
    // console.log('Seconds diff', seconds)
    if (seconds < 300) return 'Just now'
    else if (seconds < 3600) return 'In the last hour'
    // this needs to be improved - actually today, rather than seconds in a day
    else if (seconds < 86400) return 'Today'
    else if (seconds < 160000) return 'Yesterday'
    else return 'A while ago'
}

module.exports = { timeDiffToNow }
