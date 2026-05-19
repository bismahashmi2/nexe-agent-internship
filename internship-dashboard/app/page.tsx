export default function Home() {
  const beginnerProjects = [
    {
      title: "Tool-Calling AI Agent",
      description: "An intelligent AI agent that performs mathematical operations using tool/function calling with structured JSON responses and error handling.",
      features: ["Function Calling", "JSON Responses", "Error Handling"],
      techStack: ["Python", "OpenAI Agents SDK", "Gemini API"],
      githubUrl: "https://github.com/bismahashmi2/nexe-agent-internship/tree/main/beginner/tool-calling-ai-agent",
      liveDemo: null,
    },
    {
      title: "AI Calculator Agent",
      description: "A smart calculator agent with memory capabilities that performs mathematical operations using tool-calling and structured JSON output.",
      features: ["Math Operations", "Memory", "Structured Output"],
      techStack: ["Python", "OpenAI Agents SDK", "Gemini API"],
      githubUrl: "https://github.com/bismahashmi2/nexe-agent-internship/tree/main/beginner/ai-calculator-agent",
      liveDemo: null,
    },
  ];

  const comingSoonProjects = [
    { title: "Coming Soon", description: "Exciting intermediate projects in development" },
    { title: "Coming Soon", description: "More intermediate projects on the way" },
  ];

  const advancedProjects = [
    { title: "Coming Soon", description: "Advanced AI agent projects in progress" },
    { title: "Coming Soon", description: "Complex multi-agent systems coming soon" },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900">
      {/* Hero Section */}
      <div className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-purple-500/10 via-pink-500/10 to-blue-500/10 blur-3xl"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 sm:py-32">
          <div className="text-center space-y-6">
            <h1 className="text-5xl sm:text-6xl lg:text-7xl font-bold tracking-tight">
              <span className="bg-gradient-to-r from-purple-400 via-pink-400 to-blue-400 bg-clip-text text-transparent">
                Nexe-Agent Internship Dashboard
              </span>
            </h1>
            <p className="text-xl sm:text-2xl text-gray-400 max-w-3xl mx-auto">
              AI Agent Projects Portfolio
            </p>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-24 space-y-20">
        {/* Beginner Projects */}
        <section>
          <div className="mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-white mb-3">
              Beginner Projects
            </h2>
            <div className="h-1 w-24 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full"></div>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {beginnerProjects.map((project, index) => (
              <div
                key={index}
                className="group relative bg-gradient-to-br from-gray-800/50 to-gray-900/50 backdrop-blur-sm rounded-2xl p-8 border border-gray-700/50 hover:border-purple-500/50 transition-all duration-300 hover:shadow-2xl hover:shadow-purple-500/10 hover:-translate-y-1"
              >
                <div className="absolute inset-0 bg-gradient-to-br from-purple-500/5 to-pink-500/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <div className="relative space-y-6">
                  <div>
                    <h3 className="text-2xl font-bold text-white mb-3">
                      {project.title}
                    </h3>
                    <p className="text-gray-400 leading-relaxed">
                      {project.description}
                    </p>
                  </div>

                  <div>
                    <h4 className="text-sm font-semibold text-gray-300 mb-3">
                      Features
                    </h4>
                    <div className="flex flex-wrap gap-2">
                      {project.features.map((feature, idx) => (
                        <span
                          key={idx}
                          className="px-3 py-1 bg-gray-700/50 text-gray-300 text-sm rounded-full border border-gray-600/50"
                        >
                          {feature}
                        </span>
                      ))}
                    </div>
                  </div>

                  <div>
                    <h4 className="text-sm font-semibold text-gray-300 mb-3">
                      Tech Stack
                    </h4>
                    <div className="flex flex-wrap gap-2">
                      {project.techStack.map((tech, idx) => (
                        <span
                          key={idx}
                          className="px-3 py-1 bg-gradient-to-r from-purple-500/20 to-pink-500/20 text-purple-300 text-sm rounded-full border border-purple-500/30"
                        >
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>

                  <div className="flex gap-3 pt-4">
                    <a
                      href={project.githubUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex-1 px-6 py-3 bg-white text-black font-semibold rounded-lg hover:bg-gray-200 transition-colors duration-200 text-center"
                    >
                      GitHub
                    </a>
                    {project.liveDemo && (
                      <a
                        href={project.liveDemo}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex-1 px-6 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white font-semibold rounded-lg hover:from-purple-600 hover:to-pink-600 transition-all duration-200 text-center"
                      >
                        Live Demo
                      </a>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Intermediate Projects */}
        <section>
          <div className="mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-white mb-3">
              Intermediate Projects
            </h2>
            <div className="h-1 w-24 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full"></div>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {comingSoonProjects.map((project, index) => (
              <div
                key={index}
                className="relative bg-gradient-to-br from-gray-800/30 to-gray-900/30 backdrop-blur-sm rounded-2xl p-8 border border-gray-700/30"
              >
                <div className="space-y-4 text-center">
                  <div className="inline-block px-4 py-2 bg-blue-500/10 text-blue-400 text-sm font-semibold rounded-full border border-blue-500/30">
                    Coming Soon
                  </div>
                  <h3 className="text-2xl font-bold text-gray-500">
                    {project.title}
                  </h3>
                  <p className="text-gray-600">
                    {project.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Advanced Projects */}
        <section>
          <div className="mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-white mb-3">
              Advanced Projects
            </h2>
            <div className="h-1 w-24 bg-gradient-to-r from-orange-500 to-red-500 rounded-full"></div>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {advancedProjects.map((project, index) => (
              <div
                key={index}
                className="relative bg-gradient-to-br from-gray-800/30 to-gray-900/30 backdrop-blur-sm rounded-2xl p-8 border border-gray-700/30"
              >
                <div className="space-y-4 text-center">
                  <div className="inline-block px-4 py-2 bg-orange-500/10 text-orange-400 text-sm font-semibold rounded-full border border-orange-500/30">
                    Coming Soon
                  </div>
                  <h3 className="text-2xl font-bold text-gray-500">
                    {project.title}
                  </h3>
                  <p className="text-gray-600">
                    {project.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
