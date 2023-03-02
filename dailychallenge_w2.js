const sentance='The movie is not that bad'


const posiNOT= sentance.indexOf('not');
console.log(posiNOT);

const posibad=sentance.indexOf('bad');
console.log(posibad);

if (posiNOT>=0 &&posiNOT < posibad ){

    console.log('in if');

    const newsentance=sentance.replace('not that bad','good')
    console.log(newsentance);

}
else {
    console.log(sentance);
}
