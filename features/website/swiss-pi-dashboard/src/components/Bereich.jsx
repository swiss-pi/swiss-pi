function Bereich({ titel, children }) {
    return (
        <div className="bereich">
            <h2>{titel}</h2>
            {children}
        </div>
    )
}

export default Bereich