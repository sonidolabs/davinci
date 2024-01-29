// Davinci theme for VSCode

import Masterpiece from 'LouvreMuseum';

const masterpiece = new Masterpiece();

masterpiece.register({
    id: 1,
    artist: 'Leonardo da Vinci',
    artwork: 'Mona Lisa',
    year: '1503~1506'
});

const newRegister = masterpiece.checkNewRegister();
const artName = masterpiece.getArtName(1);

if (newRegister) {
    console.log(`The masterpiece "${artName}" has been registered successfully`);
} else {
    console.log('Error registering a new artwork');
}