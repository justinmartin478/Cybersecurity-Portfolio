#!/usr/bin/env python3

import random
import json
import os
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Define color sets
TITLE_COLOR = Fore.LIGHTMAGENTA_EX
DOMAIN_COLORS = {
    "Attacks, Threats, and Vulnerabilities": Fore.RED,
    "Architecture and Design": Fore.BLUE,
    "Implementation": Fore.GREEN,
    "Operations and Incident Response": Fore.YELLOW,
    "Governance, Risk, and Compliance": Fore.CYAN
}
QUESTION_COLOR = Fore.WHITE
ANSWER_COLOR = Fore.LIGHTGREEN_EX
EXPLANATION_COLOR = Fore.LIGHTYELLOW_EX
ERROR_COLOR = Fore.LIGHTRED_EX
INFO_COLOR = Fore.LIGHTCYAN_EX

# Emojis for different elements
EMOJIS = {
    "security": "🔐",
    "question": "❓",
    "correct": "✅",
    "incorrect": "❌",
    "attack": "💥",
    "architecture": "🏗️",
    "implementation": "🛠️",
    "operations": "🔄",
    "governance": "📜",
    "multiple_choice": "🔤",
    "multiple_select": "📋",
    "scenario": "🧩",
    "tip": "💡",
    "info": "ℹ️",
    "score": "📊",
    "progress": "📈",
    "domain": "📚",
    "welcome": "👋",
    "goodbye": "👋",
    "study": "📝",
    "test": "📋",
    "start": "🚀",
    "end": "🏁",
    "input": "⌨️"
}

# Domain emojis
DOMAIN_EMOJIS = {
    "Attacks, Threats, and Vulnerabilities": EMOJIS["attack"],
    "Architecture and Design": EMOJIS["architecture"],
    "Implementation": EMOJIS["implementation"],
    "Operations and Incident Response": EMOJIS["operations"],
    "Governance, Risk, and Compliance": EMOJIS["governance"]
}

# Question type emojis
QUESTION_TYPE_EMOJIS = {
    "multiple_choice": EMOJIS["multiple_choice"],
    "multiple_select": EMOJIS["multiple_select"],
    "scenario": EMOJIS["scenario"]
}

# File to store progress and statistics
PROGRESS_FILE = os.path.join(os.path.expanduser("~"), ".security_plus_progress.json")

class SecurityPlusStudyGuide:
    def __init__(self):
        self.questions = self.load_questions()
        self.progress = self.load_progress()
        self.current_domain = None
        self.current_score = 0
        self.questions_answered = 0
        
    def load_questions(self):
        """Load all Security+ exam questions."""
        # This is a small sample of questions. In a real implementation,
        # you would load from a file or database with hundreds of questions.
        return {
            "Attacks, Threats, and Vulnerabilities": [
                {
                    "id": "atv1",
                    "type": "multiple_choice",
                    "question": "Which of the following attack types involves sending malicious emails that appear to come from trusted sources?",
                    "options": [
                        "A. Cross-site scripting",
                        "B. Phishing",
                        "C. SQL injection",
                        "D. DDoS attack"
                    ],
                    "answer": "B",
                    "explanation": "Phishing is a social engineering attack where attackers send emails that appear to come from trusted sources to trick recipients into revealing sensitive information or installing malware."
                },
                {
                    "id": "atv2",
                    "type": "multiple_select",
                    "question": "Which of the following are examples of malware? (Select all that apply)",
                    "options": [
                        "A. Virus",
                        "B. Worm",
                        "C. Firewall",
                        "D. Trojan horse",
                        "E. Antivirus software"
                    ],
                    "answer": ["A", "B", "D"],
                    "explanation": "Viruses, worms, and Trojan horses are all types of malware. Firewalls and antivirus software are security tools used to protect against malware."
                },
                {
                    "id": "atv3",
                    "type": "scenario",
                    "question": "A security analyst notices unusual outbound traffic from multiple workstations during non-business hours. The traffic is directed to a single IP address, and affected systems are experiencing degraded performance. What type of attack is most likely occurring?",
                    "options": [
                        "A. Phishing campaign",
                        "B. Botnet activity",
                        "C. Physical theft",
                        "D. DNS poisoning"
                    ],
                    "answer": "B",
                    "explanation": "The scenario describes symptoms of botnet activity. Multiple compromised workstations (bots) communicating with a command and control server during off-hours is a classic sign of botnet infection."
                }
            ],
            "Architecture and Design": [
                {
                    "id": "ad1",
                    "type": "multiple_choice",
                    "question": "Which of the following best describes the concept of defense in depth?",
                    "options": [
                        "A. Using the strongest firewall available",
                        "B. Implementing multiple layers of security controls",
                        "C. Training users to recognize security threats",
                        "D. Encrypting all sensitive data"
                    ],
                    "answer": "B",
                    "explanation": "Defense in depth is a strategy that employs multiple layers of security controls throughout an information system, providing redundancy in case one security measure fails."
                },
                {
                    "id": "ad2",
                    "type": "multiple_select",
                    "question": "Which of the following are examples of physical security controls? (Select all that apply)",
                    "options": [
                        "A. Firewall",
                        "B. Mantrap",
                        "C. Encryption",
                        "D. Security guard",
                        "E. Biometric scanner"
                    ],
                    "answer": ["B", "D", "E"],
                    "explanation": "Mantraps, security guards, and biometric scanners are physical security controls. Firewalls and encryption are logical/technical controls."
                },
                {
                    "id": "ad3",
                    "type": "scenario",
                    "question": "A company is designing a new facility that will house sensitive customer financial data. Compliance requirements mandate strict separation of duties and physical access controls. Which of the following architectural elements would BEST satisfy these requirements?",
                    "options": [
                        "A. Open floor plan with security cameras",
                        "B. Biometric access control with role-based access zones",
                        "C. Single security checkpoint at building entrance",
                        "D. Locked server cabinets in a shared data center"
                    ],
                    "answer": "B",
                    "explanation": "Biometric access control with role-based access zones provides the strongest physical security control that enforces separation of duties by restricting access to only authorized personnel based on their roles."
                }
            ],
            "Implementation": [
                {
                    "id": "impl1",
                    "type": "multiple_choice",
                    "question": "Which of the following protocols encrypts web traffic between a client and server?",
                    "options": [
                        "A. HTTP",
                        "B. FTP",
                        "C. HTTPS",
                        "D. SMTP"
                    ],
                    "answer": "C",
                    "explanation": "HTTPS (Hypertext Transfer Protocol Secure) uses TLS/SSL to encrypt web traffic between a client and server, providing confidentiality, integrity, and authentication."
                },
                {
                    "id": "impl2",
                    "type": "multiple_select",
                    "question": "Which of the following should be included in a secure password policy? (Select all that apply)",
                    "options": [
                        "A. Minimum password length requirement",
                        "B. Password history enforcement",
                        "C. Writing down passwords in a secure location",
                        "D. Complexity requirements",
                        "E. Maximum password age"
                    ],
                    "answer": ["A", "B", "D", "E"],
                    "explanation": "A secure password policy should include minimum length requirements, password history to prevent reuse, complexity requirements (mix of character types), and maximum age to force periodic changes. Writing down passwords, even in a 'secure' location, is generally not recommended."
                },
                {
                    "id": "impl3",
                    "type": "scenario",
                    "question": "A system administrator needs to implement a secure remote access solution for employees. The solution must support multi-factor authentication and encrypt all traffic. Which of the following would be the MOST appropriate implementation?",
                    "options": [
                        "A. RDP over public internet",
                        "B. SSH with password authentication",
                        "C. VPN with certificate and password authentication",
                        "D. Telnet with IP restriction"
                    ],
                    "answer": "C",
                    "explanation": "A VPN with certificate and password authentication provides encrypted tunneling for all traffic and implements multi-factor authentication (certificate = something you have, password = something you know)."
                }
            ],
            "Operations and Incident Response": [
                {
                    "id": "oir1",
                    "type": "multiple_choice",
                    "question": "Which of the following best describes the primary purpose of a SIEM system?",
                    "options": [
                        "A. To block malicious network traffic",
                        "B. To collect, analyze, and correlate security event data",
                        "C. To scan for vulnerabilities in applications",
                        "D. To encrypt sensitive data at rest"
                    ],
                    "answer": "B",
                    "explanation": "A Security Information and Event Management (SIEM) system collects logs and security event data from multiple sources, then analyzes and correlates this data to identify potential security incidents."
                },
                {
                    "id": "oir2",
                    "type": "multiple_select",
                    "question": "Which of the following are typical steps in incident response? (Select all that apply)",
                    "options": [
                        "A. Preparation",
                        "B. Identification",
                        "C. Software development",
                        "D. Containment",
                        "E. Recovery"
                    ],
                    "answer": ["A", "B", "D", "E"],
                    "explanation": "Preparation, identification, containment, and recovery are all steps in the incident response lifecycle. Software development is not typically part of incident response."
                },
                {
                    "id": "oir3",
                    "type": "scenario",
                    "question": "A security analyst receives an alert indicating unusual authentication attempts across multiple servers. Upon investigation, they discover a compromised admin account is being used to access sensitive data. What should be the FIRST response action?",
                    "options": [
                        "A. Immediately shut down all affected servers",
                        "B. Disable the compromised account and isolate affected systems",
                        "C. Restore all systems from backups",
                        "D. Call law enforcement"
                    ],
                    "answer": "B",
                    "explanation": "The first priority is containment - disabling the compromised account stops the attack, while isolating affected systems prevents further spread. This preserves evidence while stopping the attack, whereas options A and C might destroy evidence or cause unnecessary disruption."
                }
            ],
            "Governance, Risk, and Compliance": [
                {
                    "id": "grc1",
                    "type": "multiple_choice",
                    "question": "Which of the following best describes the concept of risk acceptance?",
                    "options": [
                        "A. Implementing controls to reduce risk",
                        "B. Transferring risk to another party",
                        "C. Acknowledging and taking responsibility for risk",
                        "D. Avoiding activities that incur risk"
                    ],
                    "answer": "C",
                    "explanation": "Risk acceptance is a risk management strategy where an organization acknowledges the risk and decides to accept the potential consequences rather than implement controls, transfer, or avoid the risk."
                },
                {
                    "id": "grc2",
                    "type": "multiple_select",
                    "question": "Which of the following regulations or standards are related to payment card security? (Select all that apply)",
                    "options": [
                        "A. PCI DSS",
                        "B. HIPAA",
                        "C. GDPR",
                        "D. SOX",
                        "E. PA-DSS"
                    ],
                    "answer": ["A", "E"],
                    "explanation": "PCI DSS (Payment Card Industry Data Security Standard) and PA-DSS (Payment Application Data Security Standard) are specifically focused on payment card security. HIPAA relates to healthcare data, GDPR to personal data privacy (primarily in the EU), and SOX to financial reporting."
                },
                {
                    "id": "grc3",
                    "type": "scenario",
                    "question": "A healthcare organization is implementing a new cloud-based patient portal. The security team needs to ensure compliance with relevant regulations. Which of the following should be the HIGHEST priority?",
                    "options": [
                        "A. Conducting a risk assessment and implementing appropriate controls",
                        "B. Obtaining cyber insurance",
                        "C. Publishing a privacy policy on the website",
                        "D. Disabling all cloud access from mobile devices"
                    ],
                    "answer": "A",
                    "explanation": "For a healthcare organization implementing a new system containing patient data, conducting a risk assessment and implementing appropriate controls is the highest priority to ensure HIPAA compliance and protect sensitive patient information."
                }
            ]
        }
    
    def load_progress(self):
        """Load saved progress from file."""
        if os.path.exists(PROGRESS_FILE):
            try:
                with open(PROGRESS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return self.initialize_progress()
        else:
            return self.initialize_progress()
    
    def initialize_progress(self):
        """Initialize a new progress tracking structure."""
        progress = {
            "total_questions_answered": 0,
            "correct_answers": 0,
            "domain_stats": {},
            "question_history": {},
            "last_session": None
        }
        
        # Initialize stats for each domain
        for domain in self.questions.keys():
            progress["domain_stats"][domain] = {
                "total": 0,
                "correct": 0,
                "accuracy": 0
            }
            
        return progress
    
    def save_progress(self):
        """Save progress to file."""
        self.progress["last_session"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with open(PROGRESS_FILE, 'w') as f:
                json.dump(self.progress, f)
            return True
        except:
            print(f"{ERROR_COLOR}{EMOJIS['error']} Error saving progress.")
            return False
    
    def show_statistics(self):
        """Display study statistics."""
        print(f"\n{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['score']} Your Study Statistics {EMOJIS['score']}")
        print(f"{INFO_COLOR}{'=' * 50}")
        
        total = self.progress["total_questions_answered"]
        if total > 0:
            correct = self.progress["correct_answers"]
            accuracy = (correct / total) * 100
            
            print(f"{INFO_COLOR}{EMOJIS['info']} Total Questions Answered: {total}")
            print(f"{INFO_COLOR}{EMOJIS['info']} Correct Answers: {correct}")
            print(f"{INFO_COLOR}{EMOJIS['info']} Overall Accuracy: {accuracy:.1f}%")
            
            print(f"\n{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['domain']} Domain Performance:")
            
            for domain, stats in self.progress["domain_stats"].items():
                if stats["total"] > 0:
                    domain_accuracy = (stats["correct"] / stats["total"]) * 100
                    color = DOMAIN_COLORS.get(domain, INFO_COLOR)
                    emoji = DOMAIN_EMOJIS.get(domain, EMOJIS["domain"])
                    
                    print(f"{color}{emoji} {domain}: {domain_accuracy:.1f}% ({stats['correct']}/{stats['total']})")
            
            if self.progress["last_session"]:
                print(f"\n{INFO_COLOR}{EMOJIS['info']} Last Study Session: {self.progress['last_session']}")
        else:
            print(f"{INFO_COLOR}{EMOJIS['info']} No study data available yet. Start a practice session to see statistics.")
    
    def select_domain(self):
        """Allow user to select a specific domain to focus on or all domains."""
        print(f"\n{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['domain']} Select Security+ Exam Domain:")
        
        domains = list(self.questions.keys())
        domains.append("All Domains")
        
        for i, domain in enumerate(domains, 1):
            if domain != "All Domains":
                color = DOMAIN_COLORS.get(domain, INFO_COLOR)
                emoji = DOMAIN_EMOJIS.get(domain, EMOJIS["domain"])
                print(f"{color}{i}. {emoji} {domain}")
            else:
                print(f"{Fore.WHITE}{i}. {EMOJIS['study']} {domain}")
        
        while True:
            try:
                choice = int(input(f"\n{INFO_COLOR}{EMOJIS['question']} Enter your choice (1-{len(domains)}): "))
                if 1 <= choice <= len(domains):
                    selected = domains[choice - 1]
                    if selected == "All Domains":
                        self.current_domain = None
                        print(f"{INFO_COLOR}{EMOJIS['info']} You selected: All Domains")
                    else:
                        self.current_domain = selected
                        color = DOMAIN_COLORS.get(selected, INFO_COLOR)
                        emoji = DOMAIN_EMOJIS.get(selected, EMOJIS["domain"])
                        print(f"{color}{emoji} You selected: {selected}")
                    break
                else:
                    print(f"{ERROR_COLOR}{EMOJIS['error']} Please enter a number between 1 and {len(domains)}.")
            except ValueError:
                print(f"{ERROR_COLOR}{EMOJIS['error']} Please enter a valid number.")
    
    def get_random_question(self):
        """Get a random question from the current domain or all domains."""
        if self.current_domain:
            domain_questions = self.questions[self.current_domain]
            if domain_questions:
                return random.choice(domain_questions), self.current_domain
            return None, None
        else:
            # Get a question from any domain
            all_domains = list(self.questions.keys())
            if not all_domains:
                return None, None
                
            domain = random.choice(all_domains)
            domain_questions = self.questions[domain]
            if domain_questions:
                return random.choice(domain_questions), domain
            return None, None
    
    def ask_question(self, question, domain):
        """Present a question to the user and evaluate the answer."""
        question_id = question["id"]
        question_type = question["type"]
        
        # Display question with appropriate formatting
        type_emoji = QUESTION_TYPE_EMOJIS.get(question_type, EMOJIS["question"])
        domain_color = DOMAIN_COLORS.get(domain, INFO_COLOR)
        domain_emoji = DOMAIN_EMOJIS.get(domain, EMOJIS["domain"])
        
        print(f"\n{domain_color}{domain_emoji} Domain: {domain}")
        print(f"{INFO_COLOR}{type_emoji} Question Type: {question_type.replace('_', ' ').title()}")
        print(f"{QUESTION_COLOR}{Style.BRIGHT}{EMOJIS['question']} {question['question']}")
        
        # Display options
        for option in question["options"]:
            print(f"{QUESTION_COLOR}{option}")
            
        # Get user answer based on question type
        correct = False
        user_answer = None
        
        if question_type == "multiple_choice":
            user_answer = input(f"\n{INFO_COLOR}{EMOJIS['input']} Your answer (A, B, C, D): ").strip().upper()
            correct = user_answer == question["answer"]
        
        elif question_type == "multiple_select":
            print(f"{INFO_COLOR}{EMOJIS['info']} Enter all correct options separated by commas (e.g., A,C,D)")
            user_input = input(f"{INFO_COLOR}{EMOJIS['input']} Your answer: ").strip().upper()
            user_answer = [opt.strip() for opt in user_input.split(',')]
            correct = set(user_answer) == set(question["answer"])
        
        elif question_type == "scenario":
            user_answer = input(f"\n{INFO_COLOR}{EMOJIS['input']} Your answer (A, B, C, D): ").strip().upper()
            correct = user_answer == question["answer"]
            
        # Provide feedback
        if correct:
            print(f"\n{ANSWER_COLOR}{EMOJIS['correct']} Correct!")
        else:
            print(f"\n{ERROR_COLOR}{EMOJIS['incorrect']} Incorrect.")
            
            # Show the correct answer
            if question_type == "multiple_choice" or question_type == "scenario":
                print(f"{ANSWER_COLOR}The correct answer is: {question['answer']}")
            else:  # multiple_select
                print(f"{ANSWER_COLOR}The correct answers are: {', '.join(question['answer'])}")
        
        # Show explanation
        print(f"\n{EXPLANATION_COLOR}{EMOJIS['info']} Explanation: {question['explanation']}")
        
        # Update progress
        self.questions_answered += 1
        self.progress["total_questions_answered"] += 1
        self.progress["domain_stats"][domain]["total"] += 1
        
        if correct:
            self.current_score += 1
            self.progress["correct_answers"] += 1
            self.progress["domain_stats"][domain]["correct"] += 1
        
        # Calculate and update accuracy
        domain_total = self.progress["domain_stats"][domain]["total"]
        domain_correct = self.progress["domain_stats"][domain]["correct"]
        if domain_total > 0:
            self.progress["domain_stats"][domain]["accuracy"] = (domain_correct / domain_total) * 100
        
        # Record question history
        if question_id not in self.progress["question_history"]:
            self.progress["question_history"][question_id] = {"attempts": 0, "correct": 0}
            
        self.progress["question_history"][question_id]["attempts"] += 1
        if correct:
            self.progress["question_history"][question_id]["correct"] += 1
            
        return correct
    
    def study_session(self, num_questions=10):
        """Run a study session with a specified number of questions."""
        if not self.current_domain and not any(self.questions.values()):
            print(f"{ERROR_COLOR}{EMOJIS['error']} No questions available. Please check your question database.")
            return
        
        self.current_score = 0
        self.questions_answered = 0
        
        print(f"\n{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['start']} Starting Study Session {EMOJIS['start']}")
        if self.current_domain:
            domain_color = DOMAIN_COLORS.get(self.current_domain, INFO_COLOR)
            domain_emoji = DOMAIN_EMOJIS.get(self.current_domain, EMOJIS["domain"])
            print(f"{domain_color}{domain_emoji} Domain: {self.current_domain}")
        else:
            print(f"{INFO_COLOR}{EMOJIS['domain']} Domain: All Domains")
        
        print(f"{INFO_COLOR}{EMOJIS['info']} Number of Questions: {num_questions}")
        
        for i in range(num_questions):
            question, domain = self.get_random_question()
            if not question or not domain:
                print(f"{ERROR_COLOR}{EMOJIS['error']} No more questions available.")
                break
                
            print(f"\n{INFO_COLOR}{'=' * 50}")
            print(f"{INFO_COLOR}{EMOJIS['progress']} Question {i+1} of {num_questions}")
            
            self.ask_question(question, domain)
            
            # Save progress after each question
            self.save_progress()
            
            # Prompt to continue or exit
            if i < num_questions - 1:
                continue_choice = input(f"\n{INFO_COLOR}{EMOJIS['question']} Press Enter to continue to the next question, or type 'exit' to end the session: ")
                if continue_choice.lower() == 'exit':
                    break
        
        # Show session summary
        accuracy = 0
        if self.questions_answered > 0:
            accuracy = (self.current_score / self.questions_answered) * 100
            
        print(f"\n{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['end']} Session Summary {EMOJIS['end']}")
        print(f"{INFO_COLOR}{'=' * 50}")
        print(f"{INFO_COLOR}{EMOJIS['info']} Questions Answered: {self.questions_answered}")
        print(f"{INFO_COLOR}{EMOJIS['info']} Correct Answers: {self.current_score}")
        print(f"{INFO_COLOR}{EMOJIS['info']} Session Accuracy: {accuracy:.1f}%")
        
        if accuracy >= 90:
            print(f"{ANSWER_COLOR}{EMOJIS['correct']} Excellent! You're well-prepared for this topic.")
        elif accuracy >= 70:
            print(f"{ANSWER_COLOR}{EMOJIS['correct']} Good job! Keep studying to improve further.")
        else:
            print(f"{EXPLANATION_COLOR}{EMOJIS['study']} More study recommended for this topic.")
    
    def display_exam_tips(self):
        """Display helpful tips for the Security+ exam."""
        print(f"\n{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['tip']} Security+ Exam Tips {EMOJIS['tip']}")
        print(f"{INFO_COLOR}{'=' * 50}")
        
        tips = [
            "Read each question carefully - CompTIA is known for tricky wording.",
            "For scenario questions, identify what the scenario is asking before looking at answers.",
            "Look for keywords like BEST, MOST, LEAST, or FIRST that indicate what perspective to take.",
            "Process of elimination - if you're unsure, eliminate obviously wrong answers first.",
            "If two answers seem correct, choose the one that most directly addresses the question.",
            "For performance-based questions, read all instructions carefully before starting.",
            "Skip difficult questions and return to them later - manage your time effectively.",
            "Remember the CIA triad (Confidentiality, Integrity, Availability) for security objectives.",
            "Know the common ports and protocols - these appear frequently on the exam.",
            "Understand the difference between authentication, authorization, and accounting."
        ]
        
        for i, tip in enumerate(tips, 1):
            print(f"{INFO_COLOR}{EMOJIS['tip']} Tip {i}: {tip}")
    
    def display_menu(self):
        """Display the main menu for the study guide."""
        print(f"\n{TITLE_COLOR}{Style.BRIGHT}{'=' * 60}")
        print(f"{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['security']} CompTIA Security+ SY0-601 Study Guide {EMOJIS['security']}")
        print(f"{TITLE_COLOR}{Style.BRIGHT}{'=' * 60}")
        
        print(f"\n{INFO_COLOR}1. {EMOJIS['domain']} Select Domain")
        print(f"{INFO_COLOR}2. {EMOJIS['start']} Start Study Session")
        print(f"{INFO_COLOR}3. {EMOJIS['score']} View Statistics")
        print(f"{INFO_COLOR}4. {EMOJIS['tip']} Exam Tips")
        print(f"{INFO_COLOR}5. {EMOJIS['goodbye']} Exit")
    
    def run(self):
        """Run the main study guide application."""
        print(f"\n{TITLE_COLOR}{Style.BRIGHT}{EMOJIS['welcome']} Welcome to the CompTIA Security+ Study Guide! {EMOJIS['welcome']}")
        
        while True:
            self.display_menu()
            
            try:
                choice = int(input(f"\n{INFO_COLOR}{EMOJIS['question']} Enter your choice (1-5): "))
                
                if choice == 1:
                    self.select_domain()
                    
                elif choice == 2:
                    try:
                        num_questions = int(input(f"{INFO_COLOR}{EMOJIS['question']} How many questions would you like to study? (1-20): "))
                        if 1 <= num_questions <= 20:
                            self.study_session(num_questions)
                        else:
                            print(f"{ERROR_COLOR}{EMOJIS['error']} Please enter a number between 1 and 20.")
                    except ValueError:
                        print(f"{ERROR_COLOR}{EMOJIS['error']} Please enter a valid number.")
                        
                elif choice == 3:
                    self.show_statistics()
                    
                elif choice == 4:
                    self.display_exam_tips()
                    
                elif choice == 5:
                    print(f"\n{TITLE_COLOR}{EMOJIS['goodbye']} Thank you for using the Security+ Study Guide! Good luck on your exam! {EMOJIS['security']}")
                    break
                    
                else:
                    print(f"{ERROR_COLOR}{EMOJIS['error']} Please enter a number between 1 and 5.")
                    
            except ValueError:
                print(f"{ERROR_COLOR}{EMOJIS['error']} Please enter a valid number.")
                
            # Wait for user to press Enter before showing menu again
            input(f"\n{INFO_COLOR}Press Enter to continue...")

if __name__ == "__main__":
    guide = SecurityPlusStudyGuide()
    guide.run()

