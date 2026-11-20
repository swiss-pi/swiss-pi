import ToolSeite from '../components/ToolSeite.jsx'

function Mitre() {
    return (
        <ToolSeite
            titel="Swiss-Pi-Mitre Att&ck"
            kacheln={[
                { name: 'Erkannte Techniken', wert: '–' },
                { name: 'Taktiken', wert: '–' },
                { name: 'Events zugeordnet', wert: '–' },
                { name: 'Häufigste', wert: '–' },
            ]}
        />
    )
}

export default Mitre