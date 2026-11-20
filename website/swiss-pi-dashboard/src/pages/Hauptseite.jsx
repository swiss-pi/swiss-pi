import { Link } from 'react-router-dom'
import Menue from '../components/Menue.jsx'
import Kachel from '../components/Kachel.jsx'
import Bereich from '../components/Bereich.jsx'
import './Hauptseite.css'

function Hauptseite() {
    return (
        <div className="hauptseite">
            <header className="kopfzeile">
                <div className="logo">
                    <img src="/swisspi-icon.png" alt="" className="logo-bild" />
                    <span className="logo-text">
                        Swiss<span className="logo-pi">Pi</span>
                    </span>
                </div>
                <Menue position="kopf" mitLogout={true} />
            </header>

            <div className="begruessung">
                <div>
                    <h1>Welcome to Swiss-Pi!</h1>
                    <p className="untertitel">Übersicht über alle Sicherheitsereignisse</p>
                </div>
            </div>

            <div className="kachel-reihe">
                <Kachel name="Critical" anzahl={0} farbe="var(--critical)" />
                <Kachel name="High" anzahl={0} farbe="var(--high)" />
                <Kachel name="Medium" anzahl={0} farbe="var(--medium)" />
                <Kachel name="Low" anzahl={0} farbe="var(--low)" />
            </div>

            <div className="bereich-reihe">
                <Bereich titel="Network Monitoring">
                    <Link to="/nmap" className="tool-button">
                        <span>
                            <strong>Nmap</strong>
                            <small>Netzwerk-Scan</small>
                        </span>
                        <span className="pfeil">→</span>
                    </Link>
                    <Link to="/suricata" className="tool-button">
                        <span>
                            <strong>Suricata</strong>
                            <small>Intrusion Detection</small>
                        </span>
                        <span className="pfeil">→</span>
                    </Link>
                </Bereich>

                <Bereich titel="Threat Intelligence">
                    <Link to="/cowrie" className="tool-button">
                        <span>
                            <strong>Cowrie</strong>
                            <small>SSH-Honeypot</small>
                        </span>
                        <span className="pfeil">→</span>
                    </Link>
                    <Link to="/mitre" className="tool-button">
                        <span>
                            <strong>MITRE ATT&amp;CK</strong>
                            <small>Angriffstechniken</small>
                        </span>
                        <span className="pfeil">→</span>
                    </Link>
                </Bereich>
            </div>
        </div>
    )
}

export default Hauptseite
 