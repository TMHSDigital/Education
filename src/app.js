const chapters = [
    { id: 1, title: "Python", path: "Chapter-1/index.html" },
    { id: 2, title: "JavaScript", path: "Chapter-2/index.html" },
    { id: 3, title: "Java", path: "Chapter-3/index.html" },
    { id: 4, title: "C#", path: "Chapter-4/index.html" },
    { id: 5, title: "Lua", path: "Chapter-5/index.html" },
    { id: 6, title: "CSS", path: "Chapter-6/index.html" },
    { id: 7, title: "C++", path: "Chapter-7/index.html" },
    { id: 8, title: "Go", path: "Chapter-8/index.html" },
    { id: 9, title: "Swift", path: "Chapter-9/index.html" },
    { id: 10, title: "Ruby", path: "Chapter-10/index.html" },
    { id: 11, title: "Kotlin", path: "Chapter-11/index.html" },
    { id: 12, title: "R", path: "Chapter-12/index.html" },
    { id: 13, title: "Tools", path: "Tools/index.html" },
    { id: 14, title: "API", path: "API/index.html" },
];

function App() {
    const [searchTerm, setSearchTerm] = React.useState('');

    const filteredChapters = chapters.filter(chapter =>
        chapter.title.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div>
            <h1>Educational Repository</h1>
            <p>Explore our comprehensive collection of programming languages, tools, and APIs.</p>
            
            <div className="search-container">
                <input
                    type="text"
                    placeholder="Search chapters..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
            </div>

            <div className="chapter-list">
                {filteredChapters.map((chapter) => (
                    <div key={chapter.id} className="chapter-item">
                        <a href={chapter.path}>{chapter.title}</a>
                    </div>
                ))}
            </div>
        </div>
    );
}