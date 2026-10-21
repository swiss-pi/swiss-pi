import { Link } from 'react-router-dom'
import Menue from '../components/Menue.jsx'
import Kachel from '../components/Kachel.jsx'
import Bereich from '../components/Bereich.jsx'
import './Hauptseite.css'

function Hauptseite() {
    return (
        <div className="hauptseite">
            <Menue position="rechts" mitLogout={true} />

            <h1>Welcome to Swiss-Pi!</h1>

            <div className="kachel-reihe">
                <Kachel name="Critical" anzahl={0} farbe="red" />
                <Kachel name="High" anzahl={0} farbe="orange" />
                <Kachel name="Medium" anzahl={0} farbe="gold" />
                <Kachel name="Low" anzahl={0} farbe="green" />
            </div>
            
            <div className="bereich-reihe">
                <Bereich titel="Network Monitoring">
                    <Link to="/nmap" className="tool-button">Nmap</Link>
                    <Link to="/suricata" className="tool-button">Suricata</Link>
                </Bereich>

                <Bereich titel="Threat Intelligence">
                    <Link to="/cowrie" className="tool-button">Cowrie</Link>
                    <Link to="/mitre" className="tool-button">Mitre Attack</Link>
                </Bereich>
            </div>
        </div>
    )
}

export default Hauptseite
